# Program for File Handling

# Function which will define the problem and ask user for choice

print('---------------------------------------File Handling---------------------------------------')

def Problem():
    print('\n')
    print('Enter 1 : To Create a File')
    print('Enter 2 : To Read a File')
    print('Enter 3 : Append a File')
    choice = input('Your Choice : ')
    return choice

def Main():
    choice = Problem()
    if choice == '1':
        CreateFile()
    elif choice == '2':
        ReadFile()
    elif choice == '3':
        AppendFile()
    else:
        print('\n')
        print('Invalid Choice')
        Main()

# Function which will Create a New File
def CreateFile():
    print('')
    file_name = input('Enter File Name : ')
    num_of_lines = int(input('Enter Number of Lines : '))
    if '.txt' in file_name:
        file = open(file_name, 'w')     # Opening File in write mode
        print('Enter File Content ({} Lines Maximum)'.format(num_of_lines))
        # Entering content in the file
        for line in range(num_of_lines):
            file_content = input('')
            file.write(file_content+'\n')    # Inserting content inside file
        file.close()                    # Closing the file
    else:
        print('\nInvalid File Name')
        print('Enter Again\n')
        Main()

# Function which will display the content of the file
def ReadFile():
    print('')
    file_name = input('Enter File Name : ')
    if '.txt' in file_name:
        file = open(file_name, 'r')     # Opening File in read mode
        print('The Content of {} file is'.format(file_name))
        print(file.read())              # printing the content of file
        file.close()                    # Closing the file
    else:
        print('\nInvalid File Name')
        print('Enter Again\n')
        Main()

# Function to append a file
def AppendFile():
    print('')
    file_name = input('Enter File Name : ')
    num_of_lines = int(input('Enter Number of Lines : '))
    if '.txt' in file_name:
        file = open(file_name, 'a')  # Opening File in append mode
        print('Enter File Content ({} More Maximum)'.format(num_of_lines))
        # Entering content in the file
        for line in range(num_of_lines):
            file_content = input('')
            file.write(file_content+'\n')  # Inserting content inside file
        file.close()  # Closing the file
    else:
        print('\nInvalid File Name')
        print('Enter Again\n')
        Main()

prog_choice = '1'
while prog_choice == '1':
    Main()
    prog_choice = input('Enter 1 : To Continue - ')
    if prog_choice != '1':
        print('Thanks')