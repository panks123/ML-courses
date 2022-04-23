# method overloding
# same name method, in same class with different parameter list

# class Addition:
#     def sum(self,a,b):
#         return a+b
#     def sum(self,a,b,c):
#         return a+b+c

# a=Addition()
# a.sum(1,2)
# a.sum(1,2,3)

# we cannot do like this in python
# So alternative for this is below : Although we are not overloading the methods but the work being done is same

class Addition:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c

        elif a!=None and b!=None :
            return a+b
        elif a!=None:
            return f"Sum is calculated with atleast two numbers but only one i.e. {a} is provided"
        else:
            return "Sum is calculated with atleast two numbers but Zero is provided"

a=Addition()
print(a.sum(1,2))
print(a.sum(3,4,5))
print(a.sum())
print(a.sum(1))

