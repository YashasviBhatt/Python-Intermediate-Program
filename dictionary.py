'''
If the letters of word CORONA(or any other) are arranged in all possible ways,
and these words are written in order of dictionary,
then WAP to print
1. Total number of words formed.
2. A certain word made from these letters and it's location.
3. All words in order of word dictionary.
'''

from itertools import permutations

def CreateWords(input_letter_list):
    perm = [''.join(i) for i in permutations(input_letter_list)]
    perm.sort()
    words = list()
    for word in perm:
        if word not in words:
            words.append(word)
    return words


def Main():
    input_word = input('Enter Base Word : ')
    print()
    input_letter_list = list()
    words = list()
    for letter in input_word:
        input_letter_list.append(letter.upper())
    print('''Enter
1. To print Total Number of Words
2. Search for a word and return it\'s location
3. To print all formed words
0. To Exit''')

    choice = input('Enter Choice : ')
    print()

    words = CreateWords(input_letter_list)

    if choice == '0':
        exit()
    elif choice == '1':
        print(len(words))
    elif choice == '2':
        search_word = input('Enter Word you want to Search for : ')
        if search_word.upper() in words:
            print('Found at location', words.index(search_word.upper())+1)
        else:
            print('Not Found')
    elif choice == '3':
        print(words)
    else:
        print('Invalid Choice')
        Main()

    return True


Main()