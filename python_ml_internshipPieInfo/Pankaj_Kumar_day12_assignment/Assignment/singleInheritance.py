class Figure:
    def setLength(self,l):
        self.length=l
    def setBreadth(self,b):
        self.breadth=b

class Rectangle(Figure):
    def getArea(self):
        return self.length*self.breadth

r1=Rectangle()
r1.setLength(10)
r1.setBreadth(20)
print("Area of the Rectangle=",r1.getArea())

r2=Rectangle()
r2.setLength(11)
r2.setBreadth(22)
print("Area of the Rectangle=",r2.getArea())