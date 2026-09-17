bill = int(input("enter bill"))
if(bill<101):
    print("low")
elif(bill>=101 and bill<300):
    print("normal")
else:
    print("high")