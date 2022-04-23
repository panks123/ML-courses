def fib(n):
    a=0
    b=1
    if(n==1):
        print(a,end=" ")
    else:
        print(a,b,end=" ")

        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c,end=" ")
    print()


fib(10)
fib(7)
fib(9)