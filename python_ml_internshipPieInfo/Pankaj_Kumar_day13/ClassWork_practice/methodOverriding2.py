class Bird:
    def __init__(self):
        print("Bird is ready....")

    def whoIsThis(self):
        print("Bird")
    
    def swim(self):
        print("Swim Faster")

class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is Ready...")
        
    def whoIsThis(self):
        print("Penguin")

    def swim(self):
        print("Run Faster")

p=Penguin()
p.whoIsThis()
p.swim()