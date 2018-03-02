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
### Uses s_set to reset the loop condition to rebuild a set 
def matrix_indep(in_matrix):
    if numpy.linalg.det(in_matrix) == 0:
        return False    
    return True

### Inputs set of primes from 2 to b, and p - prime integer limit for random number generator

def log_calculator(s_set, p):
    s_cardinality = len(s_set)                            #boundary condition for our loop
    
    alpha_vector = []
    matrix = []
    vector_count = 0

    while vector_count != s_cardinality:
        alpha = random.randint(0, p)                      
        g = 11
        g_to_the_alpha = (g ** alpha) % p

        if is_smooth(g_to_the_alpha, s_set):
            #builds alpha vectors
            alpha_vector.append(alpha)

            #builds matrix of coefficients to small DLP's
            matrix_row = matrix_builder(g_to_the_alpha, s_set)
            matrix.append(matrix_row)

            vector_count += 1

    matrix = numpy.matrix(matrix)

    if not matrix_indep(matrix):
        matrix = log_calculator(s_set, p)

    print("Now printing all coefficients of DLP's with primes <= b:\n",matrix)

    print ("\nNow printing correspodning alpha vector:\n", alpha_vector)    

    return matrix    


def index_calculus(s_set, p):
    log_calculator(s_set, p)
    
my_set = s_set(13)
index_calculus(my_set, 31)