class Room:
    def setLBH(self,l,b,h):
        self.length=l
        self.breadth=b
        self.height=h
    
class PaintCost:
    costperSqft=100

class PaintingCost(Room,PaintCost):
    def totalCost(self):
        area=2*(self.length*self.height+self.breadth*self.height)+self.length*self.breadth
        return self.costperSqft*area

c= PaintingCost()
c.setLBH(10,20,30)
print("Total Painting Cost = Rs ",c.totalCost())