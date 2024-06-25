import numpy as np

m=6
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def graphMatrix(m:int,p):
    zero_matix = np.zeros((m,m))
    for i in range(m):
        zero_matix[i][(i*p)%m]=1
    return zero_matix

# for i in range(1,11):
#     print(f"{i}x{i} has rank {np.linalg.matrix_rank(graphMatrix(i))}")


# the rank is equal to 1 when graphMatrix(i,p) corresponds to the divisors of p
# res = []
# for i in range(1,200):
#     if np.linalg.matrix_rank(graphMatrix(i,2)) == 1:
#         res.append(i)
# print(res)

# pick p such that sigma_1(p)=2p

print(np.linalg.matrix_rank(graphMatrix(35,10)))