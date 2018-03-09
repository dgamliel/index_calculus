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
    else:
        return neg

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
            
            for y in range(x, y_dim):
                if x != y:
                    pass


#This has a crazy huge Big-O runtime. (Something like O(n^5)!!!)

def new_matrix_inv(in_mat, p):
    co_factor_matrix = matrix_cofactor(in_mat)

    det = int(np.linalg.det(in_mat))
    print ("determinant of my_mat is:", det)
    print ("\nModular inverse of determinant is :", modinv(det, p))
    co_factor_matrix = matrix_cofactor(in_mat)
    print ("\nCo-factor matrix is:\n", co_factor_matrix)
    x_dim, y_dim = co_factor_matrix.shape
    for x in range(x_dim):
        for y in range(y_dim):
            co_factor_matrix[x,y] = convert_neg(co_factor_matrix[x,y], p-1)

    print ("\n",co_factor_matrix)
    co_factor_matrix = co_factor_matrix * modinv(det, p-1)
    print ("\nCo-factor matrix after inverse mod multiplication is :\n", co_factor_matrix)
    for x in range(x_dim):
        for y in range(y_dim):
            co_factor_matrix[x,y] = co_factor_matrix[x,y] % p - 1

    return co_factor_matrix

'''
Stack overflow functions that implement basic number theory programs
'''
def matrix_cofactor(matrix):
    C = np.zeros(matrix.shape)
    nrows, ncols = C.shape
    for row in range(nrows):
        for col in range(ncols):
            minor = matrix[np.array(list(range(row))+list(range(row+1,nrows)))[:,np.newaxis],
                           np.array(list(range(col))+list(range(col+1,ncols)))]
            C[row, col] = (-1)**(row+col) * np.linalg.det(minor)
    return C

def modinv(a, m) :
    a = a % m;
    for x in range(1, m) :
        if ((a * x) % m == 1) :
            return x
    return 1

# def egcd(a, b):
#     if a == 0:
#         return (b, 0, 1)
#     else:
#         g, y, x = egcd(b % a, a)
#         return (g, x - (b // a) * y, y)

# def modinv(a, m):
#     if a < 0:
#         a = convert_neg(a, m)
#     g, x, y = egcd(a, m)
#     if g != 1:
#         raise Exception('modular inverse does not exist')
#     else:
#         return x % m

### ---------- TESTING ---------- ###

test_mat = np.matrix([[1,0,2,1],
                      [1,1,1,0],
                      [0,1,2,1],
                      [1,0,1,2]])

print ("Inverse of matrix is :\n", new_matrix_inv(test_mat, 2017))
