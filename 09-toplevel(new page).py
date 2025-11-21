from tkinter import *
from tkinter import messagebox

root=Tk()

def newpage():
    top=Toplevel()
    top.geometry("200x200")
    lbl1=Label(top,text="welcome to new page!").pack()
    
    
btn=Button(root,text="click here",command=newpage).pack()




root.mainloop()