from tkinter import *

def left(event):
    print("Left clicked")

def middle(event):
    print("Middle clicked")

def right(event):
    print("Right clicked")

root=Tk()
root.geometry("300x345")
root.title("Button Events")
button=Button(root,text="Click here")
button.bind("<Button-1>",left)
button.bind("<Button-2>",middle)
button.bind("<Button-3>",right)

button.pack()

root.mainloop()
