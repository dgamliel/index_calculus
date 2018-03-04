#!/usr/bin/env python3
import numpy
from sympy import sieve, factorint
import lin_alg
import random

### Returns the set of all primes from 2 to b ###

def s_set(b):
    prime_list = sieve.primerange(2, b+1)
    # if primitive_el in prime_list:
    #     g = prime_list.index(primitive_el)
    #     del[g]
    return list(prime_list)

### Input: alpha - int ; s_set - list of prime numbers <= b

def is_smooth(alpha, s_set):             
    if alpha < 2:
        return False

    factored_dict = factorint(alpha)   #creates a dict of all prime factors as keys and exponents as values
    dict_len = len(factored_dict)   

    prime_count = 0
    for prime in factored_dict:
        if prime in s_set:
            prime_count += 1

    if dict_len == prime_count:
        return True

    return False

### Creates individual rows of matrix, each index represents the coefficient of the DLP of each prime

def matrix_builder(g_to_the_alpha, s_set):
    dict_of_factors = factorint(g_to_the_alpha)
    matrix_row = []
    for prime in s_set:
        if prime not in dict_of_factors:
            matrix_row.append(0)
        else:
            exponent = dict_of_factors[prime]
            matrix_row.append(exponent)

    return matrix_row

### Verifies that our matrix det == 0 --> each row of our matrix is independent

def matrix_dep(in_matrix):
    print ("Matrix Determinant is :", numpy.linalg.det(in_matrix))
    if numpy.linalg.det(in_matrix) == 0:
        return True    
    return False

### Creates a resultant vector (list) of the values of the DL's for each prime, with a 1-1 index mapping
### from our s_set --> result vector. Ex : since 2 == s_set[0] --> result_vector[0] == log_g(2) 

def log_values(in_tuple, p):
    matrix       = in_tuple[0]
    alpha_vector = in_tuple[1]
    matrix_inv   = mod_inv_matrix(matrix, p)

    log_values   = matrix_inv.dot(alpha_vector)
    log_values   = list(log_values)
    for i in range(len(log_values)):
        log_values[i] = int(log_values[i])
        log_values[i] = log_values[i] % p - 1
    print('Log values are : ', log_values)
    return log_values
    

def mod_inv_matrix(in_matrix, p):
    co_factor_matrix = lin_alg.matrix_cofactor(in_matrix)
    co_factor_det    = int(numpy.linalg.det(co_factor_matrix))
    print ("Cofactor determinant is :", co_factor_det)
    mod_inv          = lin_alg.modinv(co_factor_det, p)

    return_matrix    = mod_inv * co_factor_matrix
    print(return_matrix)
    return return_matrix


    
### Inputs:
#   s_set = set of primes from 2 to b
#   p     = prime number modulus
#   p_el  = primitive element of z_star; ususally our g in g ** alpha

def log_matrix(s_set, p, primitive_el):

    #defines loop conditions
    s_cardinality = len(s_set)         
    vector_count = 0

    #defines empty containers to make matrix and corresponding vectors
    #return list should only have 2 indicies, r_l[0] == matrix, r_l[1] == corresponding alpha vectors
    alpha_vector = []
    matrix = []

    while vector_count != s_cardinality:

        #generates random alpha 
        #calculates g ^ alpha mod p
        alpha = random.randint(1, p)                      
        g_to_the_alpha = (primitive_el ** alpha) % p

        if is_smooth(g_to_the_alpha, s_set):
            #builds alpha vectors
            alpha_vector.append(alpha)

            #builds matrix of coefficients to small DLP's
            matrix_row = matrix_builder(g_to_the_alpha, s_set)
            matrix.append(matrix_row)

            vector_count += 1

    matrix = numpy.matrix(matrix)

    return_tuple = (matrix, alpha_vector)
    
    if matrix_dep(matrix):
        print ("Dependent matrix found")
        return log_matrix(s_set, p, primitive_el)

    else:
        print ("Independent matrix:\n", return_tuple[0])
        return return_tuple

def index_calculus(s_set):
    g = 5
    y = 8500
    p = 37
    equation = log_matrix(s_set, p, g)      # returns the A, b in Ax=b
    log_vals = log_values(equation, p) # returns x = (A^-1)*b mod p
    list_log_vals = list(log_vals)
    for item in list_log_vals:
        item = item % p - 1
    


my_set = s_set(3)
index_calculus(my_set)