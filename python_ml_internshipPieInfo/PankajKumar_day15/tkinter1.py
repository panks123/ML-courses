# Menus and submenus
from tkinter import *
root=Tk()
root.title("Menus and sub-Menus")
root.geometry("490x560")

def option1():
    print("Option1 Menu clicked")

def save():
    print("Saved")

def saveAs():
    print("Saved as")

def prints():
    print("printed")
myMenu=Menu(root)

myMenu.add_command(label='Option1',command=option1)


# Sub menus
fileMenu=Menu(myMenu,tearoff=False)
fileMenu.add_command(label="Save",command=save)
fileMenu.add_command(label="Save As",command=saveAs)
fileMenu.add_command(label="Print",command=prints)
myMenu.add_cascade(label='File',menu=fileMenu)
root.config(menu=myMenu)

myMenu.add_command(label='Exit',command=quit)

root.mainloop()