# Function Vernam Cipher
# Created by Yashasvi Bhatt

def VernamCipher(input_message,one_time_pad) :
    if len(input_message) == len(one_time_pad) :
        print("Cipher Text : ",end='')
        for i,o in zip(input_message,one_time_pad) :
            a=ord(i)+ord(o)                             # ord is used to find the ascii value of a character
            if a>219 :
                a=a-123
                print(chr(a),end='')                    # chr is used to fetch the character from its ascii value
            else :
                print(chr(a-97),end='')
    else :
        print("Length of PT and OTP must be same")

input_message=input("Enter Plain Text : ")
one_time_pad=input("Enter One Time Pad : ")

VernamCipher(input_message,one_time_pad)
