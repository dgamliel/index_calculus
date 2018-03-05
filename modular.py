import numpy as np

'''
These are the functions that I personally wrote and tested 
'''
#inputs a negative number and modulus p. Converts negative to corresponding positive value in mod p space
def convert_neg(neg, p):
    if neg < 0:
        neg = abs(neg)
        neg = neg % p
        return p - neg

###############################################

'''
Stack overflow functions that implement basic number theory programs
'''

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    if a < 0:
        a = convert_neg(a, m)
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

### Runs in O(n^3) runtime, thank you based Stack Overflow
def matrix_cofactor(matrix):
    C = np.zeros(matrix.shape)
    nrows, ncols = C.shape
    for row in range(nrows):
        for col in range(ncols):
            minor = matrix[np.array(list(range(row))+list(range(row+1,nrows)))[:,np.newaxis],
                           np.array(list(range(col))+list(range(col+1,ncols)))]
            C[row, col] = (-1)**(row+col) * np.linalg.det(minor)
    return C


### ---------- TESTING ---------- ###

test = convert_neg(-20, 101)
modinv(-20, 101)
modinv(test, 101)