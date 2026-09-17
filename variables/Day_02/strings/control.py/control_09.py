num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
ope = str(input("enter operator"))
if(ope=="*"):
    print(num1*num2)
elif(ope=="+"):
    print(num1+num2)
elif(ope=="-"):
    print(num1-num2)
else:
    print(num1/num2)
