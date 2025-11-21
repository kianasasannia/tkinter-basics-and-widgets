from tkinter import *


top = Tk()
Lb1 = Listbox(top)
Lb1.insert(1, "Python")
Lb1.insert(2, "c#")
Lb1.insert(2, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "java")
Lb1.insert(6, "swift")

Lb1.pack()

def delete():
    Lb1.delete(ANCHOR)
    
btn = Button(top, text = "delete", command = delete)  
btn2 = Button(top, text = "insert", command = delete)  
btn.pack()  
btn2.pack() 
top.mainloop()  