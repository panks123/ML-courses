# f-string with tkinter
from tkinter import *
root=Tk()
root.geometry("400x500")
root.title("f-string with tkinter")


def onsubmit():
    print(f"Name: {nameVar.get()} Password: {passwdVar.get()}")


Label(text="Name:").grid()
Label(text="Password:").grid(row=1)
nameVar=StringVar()
passwdVar=StringVar()

nameEntry=Entry(root,textvariable=nameVar)
passwdEntry=Entry(root,textvariable=passwdVar,show='*')
nameEntry.grid(row=0,column=1)
passwdEntry.grid(row=1,column=1)
Button(text="Submit",command=onsubmit).grid()
root.mainloop()