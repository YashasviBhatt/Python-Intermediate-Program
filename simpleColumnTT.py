# Function Simple Column TT
# Created by Yashasvi Bhatt

def SimpleColumnTT(input_message,order) :
    column1,column2,column3,column4,column5,column6=[],[],[],[],[],[]
    matrix=[]
    for i, ch in zip(range(1, len(input_message) + 1), input_message):
        if i % 2 == 0:
            column2.append(ch)
            matrix.append(column2)
        elif i % 3 == 0:
            column3.append(ch)
            matrix.append(column3)
        elif i % 4 == 0:
            column4.append(ch)
            matrix.append(column4)
        elif i % 5 == 0:
            column5.append(ch)
            matrix.append(column5)
        elif i % 6 == 0:
            column6.append(ch)
            matrix.append(column6)
        else:
            column1.append(ch)
            matrix.append(column1)

    for o in order :
        print(matrix[o],end='')

input_message=input("Enter Plain Text : ")
order=[]
print('Enter Order : ')
for i in range(0,6) :
    o=int(input())
    if i>6 :
        print ("Error")
        i=i-1
        continue
    else :
        order.append(o)

SimpleColumnTT(input_message,order)
