import numpy as np
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    if a < 0:
        a = a + m
    g, x, y = egcd(a, m)
    if g != 1:
        print ("g is : ", g)
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def matrix_cofactor(matrix):
    C = np.zeros(matrix.shape)
    nrows, ncols = C.shape
    for row in range(nrows):
        for col in range(ncols):
            minor = matrix[np.array(list(range(row))+list(range(row+1,nrows)))[:,np.newaxis],
                           np.array(list(range(col))+list(range(col+1,ncols)))]
            C[row, col] = (-1)**(row+col) * np.linalg.det(minor)
    return C