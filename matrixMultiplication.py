# Program for nxn Matrix Multiplication

import numpy as np          # numpy is used to apply the mathematical tools and formulas

# Creating method for matrix creation
def CreateMatrix(size_of_matrix) :
    matrix = []
    print('Create Matrix')
    print('Enter {} rows'.format(size_of_matrix))
    print('Enter {} Elements in each row'.format(size_of_matrix))
    for size in range(0,size_of_matrix):
        matrix.append(list(map(int, input().split())))
        if len(matrix[size]) == size_of_matrix:
            continue
        else:
            print('Matrix Multiplication can only be applied on Square Matrix')
            print('Please Enter {} Elements only in Each Row'.format(size_of_matrix))
            exit()
    return matrix


size = int(input('Enter Size of Matrix : '))
first_matrix = CreateMatrix(size)
second_matrix = CreateMatrix(size)

# dot function in numpy will return dot of given 2 parameters
resultant_matrix = np.dot(first_matrix, second_matrix)

print('First Matrix')
[print(first_matrix[row]) for row in range(size)]
print('Second Matrix')
[print(second_matrix[row]) for row in range(size)]

print('Resultant Matrix after Multiplication')
[print(resultant_matrix[row]) for row in range(size)]