# Paramaterized constructor
class Computer:
    def __init__(self,cpu,ram): # parametrized constructor
        self.ram=ram
        self.cpu=cpu

    def config(self):
        print("Config is:",self.cpu,self.ram)

c1=Computer('i5','16GB')
c2=Computer('i5','4GB')

c1.config()
c2.config()