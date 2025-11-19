from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('200x250')

def isChecked():
    return Label(ws, text=f'Checkbutton is checked: , {cb.get()}').pack()
    

cb = BooleanVar()
checkme = Checkbutton(ws, text='Check Me',variable = cb, onvalue=True, offvalue=False, command=isChecked)
checkme.pack()


ws.mainloop()