from tkinter import *


def option1():
    print("Hello")

def option2():
    print("Good to see you")

def getValues():
    print(f"Username={userVal.get()} Password={passVal.get()} Remember={rememberVal.get()}")

root = Tk()
root.title("Practice")
root.geometry("700x300")
root.maxsize(900,700)
root.minsize(300,200)

myMenu=Menu(root,)
m1=Menu(myMenu,tearoff=0)
m1.add_command(label='Option1',command=option1)
m1.add_separator()
m1.add_command(label='Option2',command=option2)

myMenu.add_cascade(label='Label1',menu=m1)


Label(root,text='Welcome ! Please sign in',font="comicsansms 20 bold",padx=2,pady=2).grid(row=0,column=1)
Label(root,text='Username:',padx=2,pady=5).grid(row=1,column=1)
Label(root,text='Password',padx=2,pady=5).grid(row=2,column=1)

userVal=StringVar()
passVal=StringVar()

userEntry=Entry(root,textvariable=userVal)
passEntry=Entry(root,textvariable=passVal,show='*')
userEntry.grid(row=1,column=2)
passEntry.grid(row=2,column=2)



rememberVal=IntVar()
ckbtn=Checkbutton(root,text='Remember me',variable=rememberVal)
ckbtn.grid(row=3,column=1)

Button(root,text='Sign in',command=getValues).grid(row=4,column=1)

root.config(menu=myMenu)


root.mainloop()