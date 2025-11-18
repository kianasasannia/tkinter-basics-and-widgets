from tkinter import *

root=Tk()
root.geometry("400x700")

f=("arial",15,'bold')
def save_btn ():
    lable1=Label(root,text="hello",font=f)
    lable1.pack()
    
button_1=Button(root,
                text="save",
                background="#8764ba",
                foreground="#0009ba",
                activebackground="#ba529b",
                activeforeground="#0e8f00",
                width=10,
                font=f,
                cursor="hand2",
                command=save_btn)
button_1.pack()

root.mainloop()