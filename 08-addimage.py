from tkinter import *
from PIL import ImageTk,Image

root =Tk()
root. title("Image")

img=ImageTk.PhotoImage(Image.open("f.jpg"))
label1=Label(image=img).pack()

root.mainloop()