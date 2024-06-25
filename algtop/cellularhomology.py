import numpy as np


class CellularHomology:
    def row_echelon(A):

        # if matrix A has no columns or rows,
        # it is already in REF, so we return itself
        r, c = A.shape
        if r == 0 or c == 0:
            return A

        # we search for non-zero element in the first column
        for i in range(len(A)):
            if A[i,0] != 0:
                break
        else:
            # if all elements in the first column is zero,
            # we perform REF on matrix from second column
            B = CellularHomology.row_echelon(A[:,1:])
            # and then add the first zero-column back
            return np.hstack([A[:,:1], B])

        # if non-zero element happens not in the first row,
        # we switch rows
        if i > 0:
            ith_row = A[i].copy()
            A[i] = A[0]
            A[0] = ith_row

        # we divide first row by first element in it
        A[0] = A[0] / A[0,0]
        # we subtract all subsequent rows with first row (it has 1 now as first element)
        # multiplied by the corresponding element in the first column
        A[1:] -= A[0] * A[1:,0:1]

        # we perform REF on matrix from second row, from second column
        B = CellularHomology.row_echelon(A[1:,1:])

        # we add first row and first (zero) column, and return
        return np.vstack([A[:1], np.hstack([A[1:,:1], B]) ])
    

    def rank(matrix):
        count = 0
        row_reduced = CellularHomology.row_echelon(matrix)
        clm = matrix.shape[1]
        row = matrix.shape[0]

        if clm >> row:
            for i in range(clm-row):
                if matrix[i,i] == 0:
                    continue
                else:
                    count +=1 
            return count
        elif row >> clm:
            for i in range(row-clm):
                if matrix[i,i] == 0:
                    continue
                else:
                    count +=1 
            return count
        else:
            for i in range(row-clm):
                if matrix[i,i] == 0:
                    continue
                else:
                    count +=1 
            return count
            
    def kernel(matrix):
        row_reduced = CellularHomology.row_echelon(matrix)
        return row_reduced.shape[1] - CellularHomology.rank(matrix)
        

        
    def homology(first_bnd, second_bnd):
        rnk = CellularHomology.rank(second_bnd)
        ker = CellularHomology.kernel(first_bnd)
        hmgy = ker-rnk
        return hmgy


