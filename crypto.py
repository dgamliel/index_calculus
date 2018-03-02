from math import sqrt, ceil
import time
'''
m = ceil(sqrt(p))

baby_steps = []
small_steps = []

for i in range(m):
    baby_steps.append(g**(i*m) % p)
'''

def neat_dots():
    counter = 0
    my_string = ""
    while True:
        while counter % 2 == 0:
            time.sleep(.1)
            my_string += "."
            print(my_string)
            if len(my_string) == 15:
                counter += 1
        while counter % 2 == 1:
            time.sleep(.1)
            my_string = my_string[:-1]
            print(my_string)
            if len(my_string) == 0:
                counter += 1

neat_dots()
        

