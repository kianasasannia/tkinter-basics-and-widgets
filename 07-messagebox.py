from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("hi")

def show ():
    response=messagebox.askyesno("popup","do you want to continiue?")
    if response==1:
        lbl=Label(text="ok")
        lbl.pack()
    else:
        lbl=Label(text="cancle")
        lbl.pack()
        

btn=Button(text="click here!",command=show)
btn.pack()
root.mainloop()