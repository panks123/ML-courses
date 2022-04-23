#Event handling
from tkinter import *
def fun():
    print("It's working!")

root=Tk()
root.geometry("400x455")
root.title("Event Handling")
button=Button(root,text="Click here",command=fun,bg="CYAN")
button.pack()

root.mainloop()