'''
Write a program that prompts for a file name,
then opens that file and reads through the file,
looking for lines of the form:

X-DSPAM-Confidence:    0.8475

Count these lines and extract the floating point values from each of the lines and
compute the average of those values and produce an output as shown below.
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
'''


file_name = input('Enter File Name : ')
file = open(file_name, 'r')

number_of_values = 0
addition_of_values = 0

for line in file:
    if line.startswith('X-DSPAM-Confidence:'):
        ln = line
        number_of_values += 1
        for character in ln:
            if character == ' ':
                index = ln.index(character)
                addition_of_values += float(ln[index+1:])

print('Average spam confidence:', addition_of_values/number_of_values)