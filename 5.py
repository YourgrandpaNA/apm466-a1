import numpy as np
import scipy.linalg as la

#a19 = [0.1, 0.19, 0.23, 0.36, 0.5]
#a20 = [0.12, 0.2, 0.24, 0.38, 0.5]
#a21 = [0.13, 0.2, 0.25, 0.38, 0.52]
#a22 = [0.12, 0.2, 0.24, 0.38, 0.51]
#a23 = [0.14, 0.15, 0.26, 0.36, 0.48]
#a24 = [0.14, 0.2, 0.24, 0.36, 0.48]
#a25 = [0.12, 0.19, 0.22, 0.35, 0.46]
#a26 = [0.12, 0.19, 0.23, 0.36, 0.48]
#a27 = [0.12, 0.18, 0.24, 0.37, 0.49]
#a28 = [0.11, 0.18, 0.23, 0.36, 0.48]

#retrn1 = np.log(a20) - np.log(a19)
#retrn2 = np.log(a22) - np.log(a21)
#retrn3 = np.log(a24) - np.log(a23)
#retrn4 = np.log(a26) - np.log(a25)
#retrn5 = np.log(a28) - np.log(a27)


#matx = [0.18232155679395445, ]


#log_return = np.log()
x1 = []

def log_return(l):
    i = 0
    ss = []
    while i < len(l):
        ss.append(np.log(l[i+1]) - np.log(l[i]))
        i += 2
    return ss



if __name__ == "__main__":
    l1 = [0.1,0.12,0.13,0.12,0.14,0.14,0.12,0.12,0.12,0.11]
    l2 = [0.19, 0.2, 0.2, 0.2, 0.15, 0.2, 0.19, 0.19, 0.18, 0.18]
    l3 = [0.23, 0.24, 0.25, 0.24, 0.26, 0.24, 0.22, 0.23, 0.24, 0.23]
    l4 = [0.36, 0.38, 0.38, 0.38, 0.36, 0.36, 0.35, 0.36, 0.37, 0.36]
    l5 = [0.5, 0.5, 0.52, 0.51, 0.48, 0.48, 0.46, 0.48, 0.49, 0.48]
    row1 = log_return(l1)
    row2 = log_return(l2)
    row3 = log_return(l3)
    row4 = log_return(l4)
    row5 = log_return(l5)
    matrx = np.row_stack((row1, row2, row3, row4, row5))
    cov = np.cov(matrx)
    print(cov)


#6
    #print(la.eig(cov))







