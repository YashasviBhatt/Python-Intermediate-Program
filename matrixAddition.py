# Program for Matrix Addition

from operator import add

# Creating Method which will create Matrix
def CreateMatrix(size):
    matrix = []
    print('Enter {} Rows'.format(size))
    print('Enter Values in the row in Single Line Separated with Space')
    for column in range(0, size):
        row = list(map(int, input().split()))          # it allows the user to input the values in single line
        # map() function returns an iterator after applying given function
        # for above case the given function is type casting to int
        matrix.append(row)
    return matrix

# Creating method which will evaluate the formed matrices
def EvaluateMatrices(first_matrix, second_matrix, size):
    for row in range(0,size):
        if len(first_matrix[row])==len(second_matrix[row]):
            if row==0:
                continue
            else:
                if len(first_matrix[row-1])==len(first_matrix[row]):
                    continue
                else:
                    print('Number of Elements in Each Row must be same')
                    exit()
        else:
            print('Values Stored in Matrices are not in Equal Number')
            exit()
    return True


def MatrixAddition(first_matrix, second_matrix):
    size = len(first_matrix)
    resultant_matrix=[]
    for row in range(0, size):
        resultant_matrix.append(list(map(add, first_matrix[row], second_matrix[row])))
    return resultant_matrix

def matrix_print(first_matrix, second_matrix, resultant_matrix):
    size=len(first_matrix)
    print('\nFirst Matrix')
    [print(first_matrix[row]) for row in range(0, size)]
    print('\nSecond Matrix')
    [print(second_matrix[row]) for row in range(0, size)]
    print('\nResultant Matrix after addition')
    [print(resultant_matrix[row]) for row in range(0, size)]
    return True


size=int(input('Enter Number of Columns : '))
print('\nEnter First Matrix')
first_matrix=CreateMatrix(size)
print('\nEnter Second Matrix')
second_matrix=CreateMatrix(size)
EvaluateMatrices(first_matrix, second_matrix, size)
resultant_matrix=MatrixAddition(first_matrix, second_matrix)
matrix_print(first_matrix, second_matrix, resultant_matrix)