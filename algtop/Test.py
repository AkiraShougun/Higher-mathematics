from cellularhomology import CellularHomology as CH
import numpy as np


d_0 = np.array([[1,0],[0,1]])
d_1 = np.array([[1,0,-1,0],[-1,0,1,0]],dtype=int)
d_2= np.array([[0,0],[1,1],[0,0],[1,1]],dtype=int)
d_3 = np.array([[1,0],[0,1]])


def main():
    print(CH.homology(d_2,d_3))
if __name__ == "__main__":
    main()




    


