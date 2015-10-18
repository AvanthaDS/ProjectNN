__author__ = 'Avantha'
import math
import random


# Trying to calculate the back propagation calculations
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

    def dum_o_error(self):
        target = self.outVal
        out = self.oval_list
        i = 1

        while i <= len(target):
            er = (target[i - 1] - out[i - 1]) * (1 - out[i - 1]) * out[i - 1]
            self.err.append(er)
            i += 1
        return self.err

class NewWCalc:
    def __init__(self, w, err, prev_o, lrn):
        self.new_w = []
        self.lrn_rate = lrn
        self.w = w
        self.err = err
        self.prev_o = prev_o
        self.num_w = len(self.w)

    def dum_w_new(self):
        i = 1
        for x in self.err:
            for y in self.prev_o:
                # print(self.w[i - 1], x, y)
                self.new_w.append(self.w[i - 1] + (self.lrn_rate * x * y))
                i += 1
        return self.new_w

class HidnErroCalc:
    def __init__(self, nout, new_outw, outerr):
        w_product = []
        self.newoutw = new_outw
        self.hdnout = nout
        self.out_er = outerr
        self.brk = len(self.hdnout)
        self.newr_out_errs = []

    def out_errors(self):
        i = 0
        for x in self.hdnout:
            k = 0
            out_w_prods = []  # to store the out put to weight product
            for y in self.out_er:
                product = y * self.newoutw[i + k]
                out_w_prods.append(product)
                k += self.brk
            i += 1

            output_err = x * (1 - x) * sum(out_w_prods)
            self.newr_out_errs.append(output_err)

        return self.newr_out_errs


# user inputs !!! Makesure the same function is not called twice this will create more lists !!!!
ads_input_vals = [0.1, 0.7]  # input list
ads_target_out = [0.3, 0.4]  # output list
ads_neurons_n = 3  # number of Neurons required
ads_lrn_rate = 1  # enter learning rate

# forward pass 1st iteration C1 - <class><number>
ads_C1 = DynamicNeuralVal(ads_input_vals, ads_neurons_n,
                          ads_target_out)  # pass the inputs to the neuron calculation class
ads_nvals = ads_C1.dum_n_cal()
ads_outvals = ads_C1.dum_out_cal()
ads_out_errs = ads_C1.dum_o_error()
print('N values:', ads_nvals)
print('Output Vals:', ads_outvals)
print('Out errors:', ads_out_errs)

# back propagation output layer weights correction
ads_output_ws = ads_C1.ouw
ads_C2 = NewWCalc(ads_output_ws, ads_out_errs, ads_nvals, ads_lrn_rate)
print('Old out wa:', ads_C1.ouw)
print('new out ws:', ads_C2.dum_w_new())

# Back propagation hidden layer error calculation
ads_new_w = ads_C2.new_w
ads_C3 = HidnErroCalc(ads_nvals, ads_new_w, ads_out_errs)
ads_hdnl_errs = ads_C3.out_errors()
print('Hidden Layer errors:', ads_hdnl_errs)

# back propagation input layer weights correction
ads_input_ws = ads_C1.inw
ads_C4 = NewWCalc(ads_input_ws, ads_hdnl_errs, ads_input_vals, ads_lrn_rate)
print('ols input ws:', ads_C1.inw)
print('New input ws:', ads_C4.dum_w_new())
