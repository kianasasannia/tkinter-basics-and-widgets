from tkinter import *

def empty():
   new = Toplevel(root)
   button = Button(new, text="click")
   button.pack()
   
root = Tk()
menu = Menu(root)
filemenu = Menu(menu)
filemenu.add_command(label="New", command=empty)
filemenu.add_command(label="Open", command=empty)
filemenu.add_command(label="Save", command=empty)
filemenu.add_command(label="Save as...", command=empty)
filemenu.add_command(label="Close", command=empty)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menu)
editmenu.add_command(label="Undo", command=empty)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=empty)
editmenu.add_command(label="Copy", command=empty)
editmenu.add_command(label="Paste", command=empty)
editmenu.add_command(label="Delete", command=empty)
editmenu.add_command(label="Select All", command=empty)

menu.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menu)
helpmenu.add_command(label="Help Index", command=empty)
helpmenu.add_command(label="About...", command=empty)
menu.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menu)
root.mainloop()