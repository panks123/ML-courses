a=int(input("Enter the first no.: "))
b=int(input("Enter the second no.: "))
print("Before swapping : ")
print("First no.=",a)
print("Second no.=",b)

a=a+b
b=a-b
a=a-b
print("After swapping : ")
print("First no.=",a)
print("Second no.=",b)