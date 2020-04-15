# Program to find the Natural Number Equivalent of a Roman Number under 3000

# method to evaluate the entered roman number
# rule 1 : Entered Roman must only contains letters like I, V, X, L, C, D, M
# rule 2 : A letter can only be appeared max 3 times at a time
# rule 3 : Letters like V, L, D cannot appear more than 1 times
# rule 4 : In whole expression the max occurrence limit of any letter is only 3
def EvaluateRoman(input_roman_number):
    roman_lst = {}

    for str_ptr in input_roman_number:
        flag = 0
        for lst_ptr in range(len(roman)):
            if str_ptr == roman[lst_ptr]:
                flag = 1

    if flag == 0:
        print('Invalid Roman Entered')
        exit()

    for ptr in range(len(input_roman_number)):
        if ptr >= 3:
            if input_roman_number[ptr] == input_roman_number[ptr - 1] == input_roman_number[ptr - 2] == \
                    input_roman_number[ptr - 3]:
                print('Invalid Roman Entered')
                exit()

    for str_ptr in input_roman_number:
        if not str_ptr in roman_lst:
            roman_lst[str_ptr] = 1
        else:
            roman_lst[str_ptr] += 1

    for str_ptr in input_roman_number:
        if str_ptr == 'V' or str_ptr == 'L' or str_ptr == 'D':
            if roman_lst[str_ptr] > 1:
                print('Invalid Roman Entered')
                exit()

    for dict_ptr in roman_lst:
        if roman_lst[dict_ptr] > 4:
            print('Invalid Roman Entered')
            exit()

# Creating method which will return the Natural Equivalent of the Inserted Roman Number
# rule 1 : if I comes before X or V then the resultant number is 9 or 4 resp.
# rule 2 : if I comes before C or L then the resultant number is 90 or 40 resp.
# rule 1 : if I comes before M or D then the resultant number is 900 or 400 resp.
def Equivalent(input_roman_number) :
    integer_number = 0
    str_ptr1 = ''

    for str_ptr in input_roman_number:
        if str_ptr in roman:
            int_ptr = roman.index(str_ptr)
            integer_number += integer[int_ptr]
            if (str_ptr == 'M' and str_ptr1 == 'C') or (str_ptr == 'D' and str_ptr1 == 'C') :
                integer_number-=200
            if (str_ptr == 'C' and str_ptr1 == 'X') or (str_ptr == 'L' and str_ptr1 == 'X'):
                integer_number -= 20
            if (str_ptr == 'X' and str_ptr1 == 'I') or (str_ptr == 'V' and str_ptr1 == 'I') :
                integer_number -= 2
            str_ptr1 = str_ptr
    return integer_number

roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
integer = [1, 5, 10, 50, 100, 500, 1000]

input_roman_number = input('Enter Roman Number : ')
input_roman_number = input_roman_number.upper()

EvaluateRoman(input_roman_number)
integer_equivalent = Equivalent(input_roman_number)
print('Integer_Equivalent is :',integer_equivalent)