num1=float(input("enter frist number :"))
num2=float(input("enter second number :"))
num3=float(input("enter third number :"))


if(num1>num2  and num1>num3):
    print("the greatest number is ",num1)
elif(num2>num1 and num2>num3):
    print("the greatest number is ",num2)
else:
    print("the greatest number is :",num3)        