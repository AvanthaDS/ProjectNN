__author__ = 'Avantha'

import os
from tkinter import *

def ButtonHide():
    but_01.grid_forget()
    but_02.grid_forget()
    but_03.grid_forget()

def ButVisible():
    but_01.grid(row=4,column=4)
    but_02.grid(row=5,column=4)
    but_03.grid(row=6,column=4)

root=Tk()

root.wm_title('Neural Network Project Information')

lbl_01 = Label(root, text='Set Project Information')
lbl_02 = Label(root, text='Project Name')
lbl_03 = Label(root, text='Description')

ent_01 = Entry(root, width=27)
ent_02 = Text(root, width=20, height =3)

but_01 = Button(root, width=12, text='Train Net',bg = 'dark gray')
but_02 = Button(root, width =12, text='Validate Net',bg = 'dark gray')
but_03 = Button(root, width =12, text='Predict Net', bg = 'dark gray')
but_04 = Button(root, width=12, text='Create Project', bg = 'dark gray', command=ButVisible)

ButtonHide()


lbl_01.grid(row=0, sticky=W)
lbl_02.grid(row=2, sticky=W)
lbl_03.grid(row=4, sticky=W)
ent_01.grid(row=2,column=2)
ent_02.grid(row=4,column=2)

but_01.grid(row=4,column=4)
but_02.grid(row=5,column=4)
but_03.grid(row=6,column=4)
but_04.grid(row=6,column=0)






root.mainloop()