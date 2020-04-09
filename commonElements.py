# Program to find common element in n list

num_of_list = int(input('Enter Number of Lists : '))
print('Enter {} Lists'.format(num_of_list))
print('One List in One Line')
main_list = list()
elements_dict = {}

# verifying whether an element in one list is entered multiple time
for lst in range(num_of_list):
    dummy_list = list(map(int, input().split()))
    verify_list = list()
    for element in dummy_list:
        if element not in verify_list:
            verify_list.append(element)
        else:
            print('Don\'t insert same element in one list')
            exit()
    main_list.append(dummy_list)

# inserting key and values in dictionary to check how many times an element comes in either of the list
for lst in range(num_of_list):
    for element in main_list[lst]:
        if element not in elements_dict:
            elements_dict[element] = 1
        else:
            elements_dict[element] += 1

# printing common elements
flag = 0
print('Common Elements are')
for element in elements_dict:
    if elements_dict[element] == num_of_list:
            print(element, end=' ')
            flag = 1
if flag == 0:
    print('No Common Element Found')
