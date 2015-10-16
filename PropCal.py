__author__ = 'Avantha'
import math
import random


# Trying to calculate the output's and first error
# Number of input weight = number of inputs x Neurons
# Number if output weights = number of outputs Neurons

class DynamicNeuralVal:
    w = []
    inw = []
    ouw = []

    def __init__(self, in_lst, nof_n, out_lst):

        # defining the class variables
        self.inVal = in_lst
        self.outVal = out_lst
        self.num_in = len(self.inVal)  # number of inputs
        self.num_N = nof_n  # number of Neurones
        self.num_out = len(self.outVal)  # number of outputs
        self.num_inw = len(self.inVal) * self.num_N  # number of input weights (number of inputs x number of neurons)
        self.num_ouw = len(self.outVal) * self.num_N  # number of output weights (number of outputs x number of neurons)
        self.nval_list = []  # this will be populated from the output calculation function
        self.oval_list = []  # this will be populated from the output calculation function
        self.err = []

        # assigning random weights for the input synapse
        i = 1
        while i <= self.num_inw:
            self.inw.append(round(random.random(), 3))
            i += 1

        # assigning random weights for the output synapse
        j = 1
        while j <= self.num_ouw:
            self.ouw.append(round(random.random(), 3))
            j += 1

        # calculating the neuron values

    def dum_n_cal(self):
        n_product = []
        i = 1
        while i <= self.num_inw:
            for x in self.inVal:
                n_product.append(x * self.inw[i - 1])    # This will create a list 'n_product'
                i += 1                                   # and add the product of Input value in to the weight.
        k = 0.0
        n_val_lst = []
        brk = self.num_in

        while k < len(n_product):
            n_sum = sum(n_product[int(k):int(k + brk)])  # break the series N in to chuncks and create the summation
            n_val = 1 / (1 + math.exp(n_sum * -1))  # calculate the neron value
            n_val_lst.append(n_val)  # add the neuron value to a list
            k += brk

        self.nval_list = n_val_lst  # passing the neuron value list to output calculation
        return self.nval_list  # not important its defined for debugging purposes

    def dum_out_cal(self):
        val_neuron = self.nval_list
        o_product = []
        i = 1
        while i <= self.num_ouw:
            for x in val_neuron:
                o_product.append(x * self.ouw[i - 1])
                i += 1
        k = 0.0
        out_val_last = []
        brk = len(val_neuron)

        while k < len(o_product):
            o_sum = sum(o_product[int(k):int(k + brk)])
            o_val = 1 / (1 + math.exp(o_sum * -1))
            out_val_last.append(o_val)
            k += brk

        self.oval_list = out_val_last
        return self.oval_list

    def o_error(self):
        target = self.outVal
        out = self.oval_list
        i = 1

        while i <= len(target):
            er = (target[i - 1] - out[i - 1]) * (1 - out[i - 1]) * out[i - 1]
            self.err.append(er)
            i += 1
        return self.err


# user inputs
in_l = [0.1, 0.7]  # input list
out_l = [1, 1]  # output list
n_num = 2  # number of Neurons required

av2 = DynamicNeuralVal(in_l, n_num, out_l)  # pass the inputs to the neuron calculation class

av2.dum_n_cal()
print(av2.inVal)
print(av2.inw)
print(av2.ouw)
print(av2.dum_n_cal())
# av2.dum_out_cal(av2.dum_n_cal())
print(av2.dum_out_cal())
print(av2.o_error())









'''

def NuralVal(v_in1, v_in2, w1, w2):
    f = ((v_in1 * w1) + (v_in2 * w2))
    Nuron = 1 / (1 + math.exp(f*-1))
    return Nuron


def error_out(tgt, out):
    res_error = (tgt - out) * (1 - out) * out
    return res_error


def error_nuron(prevEr, prevW, out):
    NuronError = out * (1 - out) * (prevEr * prevW)
    return NuronError


def new_w(w, er, prev_out):
    w_new = w + (ln_rate * er * prev_out)
    return w_new

while  i<=100:
    A.append(NuralVal(a, b, xa[i], ya[i]))
    B.append(NuralVal(a, b, xb[i], yb[i]))
    alpha.append(NuralVal(A[i], B[i], aa[i], ba[i]))
    er.append(error_out(exp, alpha[i]))
    aa.append(new_w(aa[i], er[i], A[i]))
    ba.append(new_w(ba[i], er[i], B[i]))
    A_err.append(error_nuron(er[i], aa[i+1], A[i]))
    B_err.append(error_nuron(er[i], ba[i+1], B[i]))
    xa.append(new_w(xa[i], A_err[i], a))
    ya.append(new_w(ya[i], A_err[i], a))
    xb.append(new_w(xb[i], B_err[i], b))
    yb.append(new_w(yb[i], B_err[i], b))

    #print('A is :',A[i])
    #print('B is :',B[i])
    #print('value for output:', alpha[i])
    print('Error:', er[i], 'Output:', alpha[i])

    #print(aa[i+1], ba[i+1])
    #print(A_err[i], B_err[i])
    #print('', xa[i+1], '\n', ya[i+1], '\n', xb[i+1], '\n', yb[i+1])

    i += 1
'''


