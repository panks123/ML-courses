from tkinter import *
root =Tk()
root.geometry("300x400")
root.title("Tkinter2")


def submit():
    print("Submitted!")
name=Label(root,text="Name:")
email=Label(root,text="Email:")
passw=Label(root,text="Password")
entry1=Entry(root)
entry2=Entry(root)
entry3=Entry(root)
name.grid(row=0)
email.grid(row=1)
passw.grid(row=2)
entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)
entry3.grid(row=2,column=1)
check=Checkbutton(root,text="Keep me logged in!")
check.grid(columnspan=2)
b=Button(root,text="Submit",bg="cyan",command=submit)
b.grid(columnspan=2)

root.mainloop()