
num=int(input("Enter a number:"))
n=num
fact=1
while(n>=1):
    fact=fact*n
    n-=1
print(str(num)+"!=",fact)