__author__ = 'Avantha'

import os
from tkinter import *

def hide_me():
    butt04.pack_forget()

def hide_grid():
   butt03.grid_forget()



root = Tk()
root.wm_title('NeuralNetwork Console')
canvas = Canvas(root, width=600, height=400)
canvas.pack()
topFrame = Frame(root)
topFrame.pack()
botFrame = Frame(root)
botFrame.pack(side=BOTTOM)

class first_tab:
   def __init__(self,var,c):
      avar = var
      bt1 = Button(topFrame, text =avar+'1')
      bt2 = Button(topFrame, text =avar+'2')
      bt1.grid(row=0, column =c)
      bt2.grid(row=0, column =c+1)


ads1 = first_tab('a',1)
ads2 = first_tab('b',3)






butt03 = Button(topFrame, text='BUT03', fg='brown', command=hide_me)
butt04 = Button(botFrame, text='BUT04', bg='green', command=hide_grid)

butt03.grid(row=0, sticky=E)
butt04.pack(side=BOTTOM)

root.mainloop()
