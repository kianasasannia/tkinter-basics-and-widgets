from tkinter import *
root=Tk()
root.title("python")
label_1=Label(root,text="Hello",font=("arial",20,"bold"),background="#ba9188",foreground="purple",width=15,height=5)
# label_1.pack()
# label_1.place(x=500,y=500)
label_1.grid(row=1,column=2)

root.title("python")
label_2=Label(root,
              text="python",
              font=("arial",20,"bold"),
              background="pink",
              foreground="purple",width=15,height=5)


label_2.grid(row=2,column=2,pady=10)

root.mainloop()
