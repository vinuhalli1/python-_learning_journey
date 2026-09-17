num = int(input("enter number:"))
if(num%2 ==0 and num>0):
    print("positive even")
elif(num>0 and num%2!= 0):
    print("positive odd")
elif(num<0 and num%2==0):
    print("negative even")
elif(num<0 and num%2!=0):
    print("negative odd")
else:
    print("zero")