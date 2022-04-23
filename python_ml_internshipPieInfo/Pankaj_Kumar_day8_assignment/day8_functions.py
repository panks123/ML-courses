# functions
def greet():
    print("Hello")

greet()

def add(a,b):
    print("Addition:",a+b)

add(1,2)

def add1(a,b):
    return a+b

print(add1(1,4))

def add_sub(a,b):
    c=a+b
    d=a-b
    return c,d

r1,r2=add_sub(99,55)
print(r1,r2)
