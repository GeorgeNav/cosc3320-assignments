import os
import time
import random
from matrices import *

os.system('clear')  # For Linux/OS X
r = int(input("Make random matrices? yes(1) or no(0): "))
if r == 1:
    size = int(input("Enter a # of random matrices to multiply: "))
    M = []  # all matrices
    M_sizes = []  # all sizes for matrices

    col = random.randint(1, 10)
    m = 0
    while(m < size):
        row = col
        col = random.randint(1, 10)
        M_sizes.append([row, col])
        M.append(
            [[random.randint(0, 9) for _ in range(row)]
                for _ in range(col)])
        m += 1
        # print(M_sizes[-1])
        # for row in M[-1]:
        #    print('\t' + str(row))
        # print('\n')

    p = [tuple[0] for tuple in M_sizes]
    M_size = len(M)
    p.append(M_sizes[-1][1])
elif r == 0:
    p = list(map(int,input("Enter p values (example: '6 2 3 5') : ").split()))
print('All p values: {0}'.format(p))
print('Number of matrices: {0}'.format(len(p)-1))

minimum = scalar_multiplications(p, 'min')
average = scalar_multiplications(p, 'avg')
maximum = scalar_multiplications(p, 'max')

print('Min scalar multiplications: {0}'.format(minimum))
print('Average scalar multiplications: {0}'.format(average))
print('Max scalar multiplications: {0}'.format(maximum))
