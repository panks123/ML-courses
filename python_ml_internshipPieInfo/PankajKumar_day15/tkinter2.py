# Images using tkinter
from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.title("Images")
root.geometry("490x560")
# photo=PhotoImage(file='pankaj1.png')
# Label(image=photo).pack()

# for jpg images
img=Image.open("image1.jpg")
photo=ImageTk.PhotoImage(img)
Label(image=photo).pack()

root.mainloop()