#find the greated number among the 3 numbers
number1=int(input("Enter your Number 1:"))
number2=int(input("Enter your Number 2:"))
number3=int(input("Enter your Number 3:"))
if(number1>number2):
    if(number1>number3):
        print("Number 1 whose value is ",number1,"Is greatest")
    else:
        print("Number 2 whose value is ",number2,"Is greatest")
elif(number2>number1):
    if(number2>number3):
        print("Number 2 whose value is ",number2,"Is greatest")
    else:
        print("Number 3 whose value is ",number3,"Is greatest")
else:
    print("Number 3 whose value is ",number3,"Is greatest")