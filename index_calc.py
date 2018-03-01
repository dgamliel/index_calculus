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

    factored_dict = factorint(alpha)   #creates a dict of all prime factors as keys and exponents as values
    dict_len = len(factored_dict)   

    prime_count = 0
    for prime in factored_dict:
        if prime in s_set:
            prime_count += 1

    if dict_len == prime_count:
        return True

    return False


### Inputs set of primes from 2 to b, and p - prime integer limit for random number generator

def log_calculator(s_set, p):
    s_cardinality = len(s_set)                            #boundary condition for our loop
    vector_count = 0

    while vector_count != s_cardinality:
        alpha = random.randint(0, p)                      #picks a random alpha to be used as exponent for primitive base
        
        g = 11
        g_to_the_alpha = (g ** alpha) % p

        if is_smooth(g_to_the_alpha, s_set):
            print("alpha is : ", alpha)

            x_prime_factors = factorint(g_to_the_alpha)   #creates a dict, x_prime_factors, that contains all the prime factors of our smooth g ** a 
            
            vector_count += 1

def index_calculus(s_set, p):
    log_calculator(s_set, p)
my_set = s_set(13)
index_calculus(my_set, 31)