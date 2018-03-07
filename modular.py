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

#############################################
#            MATRICIES AAAAAAA              #
#############################################


#Inputs : Numpy matrix - A, integer modulus p 
#Output : Numpy matrix - A^-1 (A inverse)
def create_inverse(in_matrix, p):
    #returns (m, n) tuple of matrix with (m x n) dimmensions
    x_dim, y_dim = in_matrix.shape

    #checks if the matrix is square, if not, exit
    if x_dim != y_dim:
        raise Exception("Non-square matrix is non-invertible")

    #real code to create inverse
    else:
        identity_mat = np.identity(x_dim)
        
        for x in range(x_dim):
            diagonal = in_matrix[x, x]

            #find mod inverse to 
            scalar = modinv(diagonal, p)
            
            in_matrix[x] = (in_matrix[x] * scalar) % p
            identity_mat[x] = (identity_mat[x] * scalar) % p
            print (in_matrix[x])


        

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

# test = convert_neg(-20, 101)
# modinv(-20, 101)
# modinv(test, 101)

my_mat = np.matrix([[5, 3],
                   [-3, 5]])

create_inverse(my_mat, 101)