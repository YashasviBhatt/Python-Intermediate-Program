# Program to check whether a string having parenthesis is correct or not

# Method which will separate parenthesis with characters
def Parenthesis(string):
    parenthesis_list = list()
    parenthesis_occurrence = list()
    for parenthesis in string:
        if parenthesis not in parenthesis_occurrence:
            parenthesis_occurrence.append(parenthesis)
        else:
            print('Invalid String')
            exit()
        if parenthesis == '[' or parenthesis == '{' or parenthesis == '(' or parenthesis == ')' or parenthesis == '}' or parenthesis == ']':
            parenthesis_list.append(parenthesis)

    return parenthesis_list

# Method which will validate the generated list from the previous function, whether it satisfy the rules or not
def Validity(parenthesis_list):
    flag = 0
    for index in range(len(parenthesis_list)):
        if parenthesis_list[index] == '(':
            if parenthesis_list[index + 1] == ')':
                flag = 1
            else:
                flag = 0

        elif parenthesis_list[index] == '{':
            if parenthesis_list[index + 1] == '}' or parenthesis_list[index + 1] == '(':
                flag = 1
            else:
                flag = 0

        elif parenthesis_list[index] == '[':
            if parenthesis_list[index + 1] == ']' or parenthesis_list[index + 1] == '{' or parenthesis_list[index + 1] == '(':
                flag = 1
            else:
                flag = 0

    if flag == 1:
        print('Valid String')
    else:
        print('Invalid String')

# Method which will call other methods
def Main():
    input_string = input('Enter String : ')         # generating the string
    parenthesis_list = Parenthesis(input_string)    # calling the Parenthesis method
    Validity(parenthesis_list)                      # calling the Validity method

# calling the Main function
Main()