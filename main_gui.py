__author__ = 'Avantha'

from tkinter import *
import os

from TrainNet import tRainNet
from validate import vAlidateNet
from Predict import pRedictNet

base = Tk()
base.wm_title('NeuralNet')
chk_bias = IntVar()
chk_plot = IntVar()

lbl_0 =Label(base,text='Project Name')
lbl_1 = Label(base, text='# of Neurons')
lbl_2 = Label(base, text='Learning Rate')
chk_1 = Checkbutton(base, text='Include Bias', variable=chk_bias)
lbl_4 = Label(base, text='Target Error')
lbl_5 = Label(base, text='Function')
chk_2 = Checkbutton(base, text='Plot Err Graph?', variable=chk_plot)

entry_0 = Entry(base)
entry_1 = Entry(base)
entry_2 = Entry(base)
entry_4 = Entry(base)
entry_5 = Entry(base)

def newProject(): # Created the folder structure
    p_name= entry_0.get()
    project_data = '_pRoject/'+p_name
    p_train ='_pRoject/'+p_name+'/data_train'
    p_validate='_pRoject/'+p_name+'/data_validate'
    p_predict ='_pRoject/'+p_name+'/data_predict'
    p_cnfg ='_pRoject/'+p_name+'/data_cnfg'
    p_analysis ='_pRoject/'+p_name+'/analysis'
    if not os.path.isdir(project_data):
        os.makedirs(project_data)
        os.makedirs(p_train)
        os.makedirs(p_validate)
        os.makedirs(p_predict)
        os.makedirs(p_cnfg)
        os.makedirs(p_analysis)

def runTrainNet():
    nn = entry_1.get()
    ln_rate = entry_2.get()
    bias = chk_bias.get()
    tgt_rate = entry_4.get()
    fn = entry_5.get()
    grph = chk_plot.get()
    fld_name = entry_0.get()
    train_net = tRainNet(nn, ln_rate, bias, tgt_rate, fn, grph,fld_name)
    train_net.tRain()

def runvAlidateNet():
    fld_name =entry_0.get()
    validate_net = vAlidateNet(fld_name)
    validate_net.vAlidateNet()

def runpRedictNet():
    fld_name =entry_0.get()
    predict_net =pRedictNet(fld_name)
    predict_net.predictN()

but_0 = Button(base, text='Create New Project',width=15, bg='dark gray', command=newProject)
but_01 = Button(base, text='Tran Network', bg='dark gray', width=15, command=runTrainNet)
but_02 = Button(base, text='Validate Network', bg='dark gray', width=15, command=runvAlidateNet)
but_03 = Button(base, text='Predict', bg='dark gray', width=15, command=runpRedictNet)

lbl_0.grid(row=0, sticky=E)
lbl_1.grid(row=1, sticky=E)
lbl_2.grid(row=2, sticky=E)
lbl_4.grid(row=4, sticky=E)
lbl_5.grid(row=5, sticky=E)

entry_0.grid(row=0, column=1)
entry_1.grid(row=1, column=1)
entry_2.grid(row=2, column=1)
chk_1.grid(row=3, columnspan=2)
entry_4.grid(row=4, column=1)
entry_5.grid(row=5, column=1)
chk_2.grid(row=5, column=2, sticky=E)

but_0.grid(row=0,column =2, sticky=E)
but_01.grid(row=1, column=2, sticky=E)
but_02.grid(row=2, column=2, sticky=E)
but_03.grid(row=3, column=2, sticky=E)

base.mainloop()
