__author__ = 'Avantha'

from tkinter import *

from TrainNet import tRainNet
from validate import vAlidate
from Predict import pRedictNet

validate_net = vAlidate()
predict_net = pRedictNet()

base = Tk()
base.wm_title('NeuralNet')
chk_bias = IntVar()
chk_plot = IntVar()

lbl_1 = Label(base, text='# of Neurons')
lbl_2 = Label(base, text='Learning Rate')
chk_1 = Checkbutton(base, text='Include Bias', variable=chk_bias)
lbl_4 = Label(base, text='Target Error')
lbl_5 = Label(base, text='Function')
chk_2 = Checkbutton(base, text='Plot Err Graph?', variable=chk_plot)

entry_1 = Entry(base)
entry_2 = Entry(base)
entry_4 = Entry(base)
entry_5 = Entry(base)


def runTrainNet():
    nn = entry_1.get()
    ln_rate = entry_2.get()
    bias = chk_bias.get()
    tgt_rate = entry_4.get()
    fn = entry_5.get()
    grph = chk_plot.get()
    train_net = tRainNet(nn, ln_rate, bias, tgt_rate, fn, grph)
    train_net.tRain()


but_01 = Button(base, text='Tran Network', bg='dark gray', width=13, command=runTrainNet)
but_02 = Button(base, text='Validate Network', bg='dark gray', width=13, command=validate_net.vAlidateNet)
but_03 = Button(base, text='Predict', bg='dark gray', width=13, command=predict_net.predictN)

lbl_1.grid(row=0, sticky=E)
lbl_2.grid(row=1, sticky=E)
lbl_4.grid(row=3, sticky=E)
lbl_5.grid(row=4, sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)
chk_1.grid(row=2, columnspan=2)
entry_4.grid(row=3, column=1)
entry_5.grid(row=4, column=1)
chk_2.grid(row=4, column=2, sticky=E)

but_01.grid(row=0, column=2, sticky=E)
but_02.grid(row=1, column=2, sticky=E)
but_03.grid(row=2, column=2, sticky=E)

base.mainloop()
