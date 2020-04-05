# Program to find the decimal equivalent of binary number having n digits

def BinaryToDecimal(bin_num,bin_len):
    # creating a list enlisted with binary codes of decimal numbers
    binary_input_list = ["{:b}".format(num) for num in range(0,2**bin_len)]
    multiplier=1
    dec_eqvlnt=0

    flag=0
    for num in binary_input_list :
        if str(bin_num)==num :
            flag=1
    if flag==0 :
        print('Invalid Binary Entered')
        exit()

    # calculating the decimal equivalent
    else :
        while bin_num>=1 :
            dec_eqvlnt+=int(bin_num%10*multiplier)
            bin_num=int(bin_num/10)
            multiplier*=2

        return dec_eqvlnt

binary_input=int(input('Enter a Binary Number : '))
bin_len=len(str(binary_input))

# calling the BinaryToDecimal function that returns a value to a variable
binary_eqvlnt=BinaryToDecimal(binary_input,bin_len)
print('The Decimal Equivalent of {} is {}'.format(binary_input,binary_eqvlnt))

# you can use bin function in python which will return bin equivalent of number
# a=int(input('Enter Binary'))
# print(bin(a))  // it will return binary equivalent with 0b at the starting if inputted number is a decimal
# print({:b}.format(a))   // it will return decimal equivalent