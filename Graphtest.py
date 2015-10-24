__author__ = 'Avantha'
from tkinter import *


class gRaph:
    def __init__(self, err_list, x_int):
        self.er_list = err_list
        self.x_int = x_int
        self.nods = []
        self.ads_list = []

    def create_nods(self):

        for x in range(0, len(self.er_list)):
            nt = x * self.x_int, self.er_list[x] * 100
            self.nods.append(nt)

        return self.nods

    def gr_plot(self):
        width = 900
        height = 500
        root = Tk()
        canvas = Canvas(root, width=width, height=height)
        canvas.pack()
        for x in range(0, width):
            x_axis = canvas.create_line(10, x * 50, width, x * 50, fill='gray')
        for y in range(0, height):
            y_axis = canvas.create_line(y * 50, 10, y * 50, height, fill='gray')

        redline = canvas.create_line(self.nods, fill='red')

        root.mainloop()

# blackline = canvas.create_line(10,10,190,80)
# redline = canvas.create_line(10,80,20,50,190,10,fill='red')

# greenBox = canvas.create_rectangle(50,50,150,80, fill='Green')

# the following line will delete the created red line
# canvas.delete(redline)
# The following will delete all teh content in the canvas
# canvas.delete(ALL)
