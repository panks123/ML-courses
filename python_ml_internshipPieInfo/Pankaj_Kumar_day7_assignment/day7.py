from array import *
arr=array('i',[])
n=int(input("Enter the length:"))
for i in range(n):
    x=int(input("Enter element:"))
    arr.append(x)
print(arr)

val=int(input("Enter element to be searched:"))
k=0
for i in arr:
    if i==val:
        print(k)
    k+=1

val=int(input("Enter element to be searched:"))
print(arr.index(val))