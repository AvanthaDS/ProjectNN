__author__ = 'Avantha'

from tkinter import *

from Test2 import c1

base = Tk()
e1 = Entry(base)
chk_var = IntVar()
c = Checkbutton(base, text='Include Bias', variable=chk_var)


# e1.focus_set()
# a = e1.get()

def callback():
    # print(e1.get()) - works
    a = e1.get()
    b = chk_var.get()
    avC1 = c1('av', b, a)
    avC1.fk()
    # print(e1.get())
    # print(a) - doesn't work


but_01 = Button(base, text='Print my name', command=callback)
but_01.grid(row=1, column=0)
e1.grid(row=0, column=0)
c.grid(row=2, columnspan=2)

base.mainloop()
