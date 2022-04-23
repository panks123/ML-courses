a=int(input("Enter the first no.: "))
b=int(input("Enter the second no.: "))
c=int(input("Enter the third no.: "))

if a>b:
    if a>c:
        print("Largest no. is: ",a)
    elif c>a:
        print("Largest no. is: ",c)
    else:
        print("largest no. is : ",a)
elif b>a:
    if b>c:
        print("Largest no. is: ",b)
    elif c>b:
        print("Largest no. is: ",c)
    else:
        print("Largest no. is: ",b)
else:
    print("Numbers are equal")