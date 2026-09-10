a = float(input("enter number:"))
b = float(input("enter number:"))

print("1. Addition")
print("2. Substraction")
print("3. multiflication")
print("4. Division")


choice = int(input("enter choice betwwen 1-4"))
if(choice == 1):
    print("result =",a + b)
elif(choice == 2):
    print("result =",a - b)
elif(choice == 3):
    print("result =",a * b)
elif(choice == 4):
    if(b !=0):
        print("result =",a/b)
    else:
        print("division by zero is not available")

else:
    print("choice is not available")