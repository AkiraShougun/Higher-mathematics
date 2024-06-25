import numpy as np


X = ["A","C","B","BC","BA","AC"]
Y = ["A", "B", "C", "D", "AB", "AC", "BC", "BD", "CD", "BCD"]
Torus = ["A","B","C","D","E","F","G",
                    "AB","AC","AD","AE","AF","AG",
                    "BC","BD","BE","BF","BG",
                    "CD","CE","CF","CG",
                    "DE","DF","DG",
                    "EF","EG",
                    "FG",
                    "ABD","ABF","ACD","ACG","AEF","AEG",
                    "BCE","BCG","BDE","BFG",
                    "CDF","CEF",
                    "DEG","DFG"]


           

def d(x):
    dim = len(max(x, key=len))
    simplex = [sorted(s for s in x if len(s)==i) for i in range(1,dim+1)]    

    bnd = []
    for spx_k, spx_kp1 in zip(simplex, simplex[1:]):
        mtx = []
        for sigma in spx_kp1:
            faces = get_faces(sigma)
            mtx.append([get_coeff(spx, faces) for spx in spx_k])
        bnd.append(np.array(mtx).T)

    return bnd
    

def get_faces(lst):
    return [lst[:i] + lst[i+1:] for i in range(len(lst))]


def get_coeff(simplex, faces):
    if simplex in faces:
        idx = faces.index(simplex)
        return 1 if idx%2==0 else -1
    else:
        return 0
    
def kernel(A, tol=1e-5):
    _, s, vh = np.linalg.svd(A)
    singular = np.zeros(vh.shape[0], dtype=float)
    singular[:s.size] = s
    null_space = np.compress(singular <= tol, vh, axis=0)
    return null_space.T

def cokernel(A, tol=1e-5):
    u, s, _ = np.linalg.svd(A)
    singular = np.zeros(u.shape[1], dtype=float)
    singular[:s.size] = s
    return np.compress(singular <= tol, u, axis=1)

def homology(boundary_ops, tol=1e-5):
    
    mm = boundary_ops[-1].shape[1]
    nn = boundary_ops[0].shape[0]
    boundary_ops.insert(0, np.ones(shape=(0, nn)))
    boundary_ops.append(np.ones(shape=(mm, 0)))

    H = []
    for del_k, del_kp1 in zip(boundary_ops, boundary_ops[1:]):
        kappa = kernel(del_k, tol)
        
        psi, _, _, _ = np.linalg.lstsq(kappa, del_kp1, rcond=None)
        
        ksi = cokernel(psi, tol)
        H.append(np.dot(kappa, ksi))

    return H
def betti(H):
    return [basis.shape[1] for basis in H]

def main():
    hom = homology(d(Torus))
    b_num = betti(hom)
    print(b_num)


if __name__ == "__main__":
    main()