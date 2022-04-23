def factorial(n):
    if n==0:
        print(1)
    else:
        f=1
        for i in range(1,n+1):
            f*=i
        print(f)


factorial(3)
factorial(7)
factorial(5)
factorial(0)