from tkinter import *
root=Tk()

entry_1=Entry(background="yellow",
              foreground="black",
              width=15,
              font=('arial',15),
              cursor="hand2"
              )
entry_1.pack()

def get ():
    a=entry_1.get()
    a=int(a)
    lable1=Label(root,text="welcome "+a)
    lable1.pack()

button_1=Button(root,
                text="save",
                background="#8764ba",
                foreground="#0009ba",
                activebackground="#ba529b",
                activeforeground="#0e8f00",
                width=10,
                font=('arial',15),
                cursor="hand2",
                command=get)
button_1.pack()
root.mainloop()
