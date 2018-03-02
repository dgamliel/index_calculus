#!/usr/bin/env python3
import numpy
from sympy import sieve, factorint
import random

### Returns the set of all primes from 2 to b ###

def s_set(b):
    prime_list = sieve.primerange(2, b+1)
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
    if numpy.linalg.det(in_matrix) == 0:
        return True    
    return False

### Creates a resultant vector (list) of the values of the DL's for each prime, with a 1-1 index mapping
### from our s_set --> result vector. Ex : since 2 == s_set[0] --> result_vector[0] == log_g(2) 

def result_vector(matrix, vector, p):
    result_vector = matrix * vector
    result_vector = list(result_vector)
    for entry in result_vector:
        entry = entry % p - 1

    return result_vector

### Inputs set of primes from 2 to b, and p - prime integer limit for random number generator

def log_matrix(s_set, p, primtive_el):
    s_cardinality = len(s_set)                            #boundary condition for our loop
    
    alpha_vector = []
    matrix = []
    vector_count = 0

    while vector_count != s_cardinality:
        alpha = random.randint(0, p)                      
        g_to_the_alpha = (g ** alpha) % p

        if is_smooth(g_to_the_alpha, s_set):
            #builds alpha vectors
            alpha_vector.append(alpha)

            #builds matrix of coefficients to small DLP's
            matrix_row = matrix_builder(g_to_the_alpha, s_set)
            matrix.append(matrix_row)

            vector_count += 1

    matrix = numpy.matrix(matrix)

    if matrix_dep(matrix):
        print ("Dependent Matrix found:\n", matrix)
        alpha_vector = []
        matrix = log_matrix(s_set, p)


    ### Print statements to see if the thing works
    #print("Now printing all coefficients of DLP's with primes <= b:\n",matrix)
    #print ("\nNow printing correspodning alpha vector:\n", alpha_vector)    

    print ("Returning independent matrix of:\n", matrix)

    alpha_vector = numpy.linalg.matrix(alpha_vector)
    matrix_inv = numpy.linalg.inv(matrix)
    re    


def index_calculus(s_set, p, primtive_el):
    y = 8500
    p = 9973
    log_matrix(s_set, p, g)
    
my_set = s_set(13)
index_calculus(my_set, 31, 11)