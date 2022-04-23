#Polymorphism
# 1.Duck Typing
#1. Duck typinng: A bird if looks like duck,which swims like a duck and quacks like a dyuck then probably it is a duck
class MyEditor:
    def execute(self):
        print("Compiling")
        print("Running...")

class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running...")


class Laptop:
    def execute(self):
        print("Compiling")
        print("Running...")
    def code(self,ide):
        ide.execute()


ide1=PyCharm()  
ide2=MyEditor()
ide1.execute()
ide2.execute()

# here both the objects when call the method 'execute' they are exactly doing the same thing so we can say that duck typing has been done here