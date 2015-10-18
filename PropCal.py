__author__ = 'Avantha'
import math
import random


# Trying to call in the input values from a file
# Number of input weight = number of inputs x Neurons
# Number if output weights = number of outputs Neurons

# C1 - N Number, Out put, Out Put error
class DynamicNeuralVal:
    def __init__(self, in_lst, nof_n, out_lst, in_ws, out_ws):

        # defining the class variables
        self.inVal = in_lst
        self.outVal = out_lst
        self.num_in = len(self.inVal)  # number of inputs
        self.num_N = nof_n  # number of Neurones
        self.num_out = len(self.outVal)  # number of outputs
        self.num_inw = len(in_ws)
        self.num_ouw = len(out_ws)
        self.inw = in_ws
        self.ouw = out_ws
        self.nval_list = []  # this will be populated from the output calculation function
        self.oval_list = []  # this will be populated from the output calculation function
        self.err = []



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

# C2 - Output layer new Ws, C4 - Input Layer new Ws
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

# C3 - Hidden Layer Error
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
ads_input_vals = [0.1, 0.7]  # input list - fix
ads_target_vals = [0.3, .4]  # output list - fix
ads_neurons_n = 3  # number of Neurons required - Fix
ads_lrn_rate = 1  # enter learning rate - Fix
ads_itn_n = 1000  # number of iterations required
ads_itn_cntr = 1
ads_in_ws = []
ads_out_ws = []
ads_abs_error = []

# Creating the initial Ws
i = 1
j = 1

while i <= len(ads_input_vals) * ads_neurons_n:
    ads_in_ws.append(round(random.random(), 3))
    i += 1

while j <= len(ads_target_vals) * ads_neurons_n:
    ads_out_ws.append(round(random.random(), 3))
    j += 1

while ads_itn_cntr <= ads_itn_n:
    # forward pass 1st iteration C1 - <class><number>
    ads_C1 = DynamicNeuralVal(ads_input_vals, ads_neurons_n, ads_target_vals, ads_in_ws,
                              ads_out_ws)  # pass the inputs to the neuron calc class
    ads_nvals = ads_C1.dum_n_cal()
    ads_outvals = ads_C1.dum_out_cal()
    ads_out_errs = ads_C1.dum_o_error()


    # back propagation output layer weights correction
    ads_output_ws = ads_C1.ouw
    ads_C2 = NewWCalc(ads_output_ws, ads_out_errs, ads_nvals, ads_lrn_rate)
    ads_new_ow = ads_C2.dum_w_new()


    # Back propagation hidden layer error calculation
    ads_new_w = ads_C2.new_w
    ads_C3 = HidnErroCalc(ads_nvals, ads_new_w, ads_out_errs)
    ads_hdnl_errs = ads_C3.out_errors()


    # back propagation input layer weights correction
    ads_input_ws = ads_C1.inw
    ads_C4 = NewWCalc(ads_input_ws, ads_hdnl_errs, ads_input_vals, ads_lrn_rate)
    ads_new_inw = ads_C4.dum_w_new()

    # print('N values:', ads_nvals)
    # print('Output Vals:', ads_outvals)
    # print('Out errors:', ads_out_errs)
    ads_tmp_err = []
    for x in ads_out_errs:
        ads_tmp_err.append(abs(x))
    #print('Absolute total error:', sum(ads_tmp_err))
    ads_abs_error.append(sum(ads_tmp_err))
    del ads_tmp_err[:]

    # print('Hidden Layer errors:', ads_hdnl_errs)
    # print('old input ws:', ads_in_ws)
    # print('New input ws:', ads_new_inw)
    # print('Old out wa:', ads_out_ws)
    # print('new out ws:',ads_new_ow)
    #print('---------------------------------------')
    ads_in_ws = ads_new_inw
    ads_out_ws = ads_new_ow
    # print(ads_in_ws)
    # print(ads_out_ws)

    ads_itn_cntr += 1
print('calculation complete')
start_err = ads_abs_error[0]
end_err = ads_abs_error[-1]
print(start_err)
print(end_err)
ads_file = 'Abs_Err_Reduction.csv'
fx = open(ads_file, 'w')
for x in ads_abs_error:
    fx.write(str(x) + '\n')
fx.close()
