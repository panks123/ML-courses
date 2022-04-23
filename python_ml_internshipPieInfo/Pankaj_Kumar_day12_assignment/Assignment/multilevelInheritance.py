class Figure:
    def setLength(self,l):
        self.length=l
    def setBreadth(self,b):
        self.breadth=b
    def setSide(self,side):
        self.side=side

class Rectangle(Figure):
    def getArea(self):
        return self.length*self.breadth

class Square(Rectangle):
    def getArea(self):
        return self.side*self.side


s1=Square()
s1.setSide(5)
print("Area of Square=",s1.getArea())


        