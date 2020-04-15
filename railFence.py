# Function Rail Fence
# Created by Yashasvi Bhatt

def RailFence(input_message) :
    list1=[]
    list2=[]
    for i,ch in zip(range(0,len(input_message)),input_message) :
        if i%2==0 :
            list1.append(ch)
        else :
            list2.append(ch)

    print("Cipher Text : ",end='')
    for ch in list1 :
        print(ch,end='')
    for ch in list2 :
        print(ch,end='')

input_message=input("Enter Plain Text : ")
RailFence(input_message)