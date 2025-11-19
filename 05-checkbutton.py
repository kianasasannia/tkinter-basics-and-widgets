from tkinter import *
from tkinter import messagebox
import tkinter

top = Tk()
Var1 = IntVar()
Var2 = IntVar()
C1 = Checkbutton(top, text = "Music", variable = Var1,
                 onvalue = 1, offvalue = 0, height=5,
                 width = 20).pack()
C2 = Checkbutton(top, text = "Video", variable = Var2,
                 onvalue = 1, offvalue = 0, height=5,
                 width = 20).pack()

def reset ():
    Var1.set(0)
    Var2.set(0)
btn=Button(top,text="reset",command=reset).pack()
top.mainloop()