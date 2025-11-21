from tkinter import *

root =Tk()
root. title("frame")
# root.geometry("400x400")

frame=LabelFrame(root,text="this is a frame",padx=10,pady=15)
frame.pack(padx=100,pady=200)

btn=Button(frame,text="click here")
btn.pack()

root.mainloop()