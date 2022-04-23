class Figure:
    def setLength(self,l):
        self.length=l
    def setBreadth(self,b):
        self.breadth=b
    def setSide(self,side):
        self.side=side

    def setBase(self,b):
        self.base=b
    def setHeight(self,h):
        self.ht=h

class Rectangle(Figure):
    def getArea(self):
        return self.length*self.breadth

class Square(Figure):
    def getArea(self):
        return self.side*self.side

class Triangle(Figure):
    def getArea(self):
        return 0.5*self.base*self.ht

s1=Square()
s1.setSide(5)
print("Area of Square=",s1.getArea())

r1=Rectangle()
r1.setLength(10)
r1.setBreadth(12)
print("Area of Rectangle=",r1.getArea())

t1=Triangle()
t1.setBase(12)
t1.setHeight(20)
print("Area of Triangle=",t1.getArea())
        