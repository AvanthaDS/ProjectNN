__author__ = 'Avantha'
import math


class DynamicNeuralVal:
    def __init__(self, in_lst, nof_n, out_lst, in_ws, out_ws, fn):

        # defining the class variables
        self.inVal = in_lst
        self.outVal = out_lst
        self.num_in = len(self.inVal)  # number of inputs
        self.num_N = nof_n  # number of Neurones
        self.num_out = len(self.outVal)  # number of outputs
        self.num_inw = len(in_ws)
        self.num_ouw = len(out_ws)
        self.function = fn
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
            if self.function == 1:
                n_val = 1 / (1 + math.exp(n_sum * -1))  # calculate the neron value : fn for sigmoid
            else:
                n_val = (-1 + math.exp(2 * n_sum)) / (1 + math.exp(2 * n_sum))  # fn for Hypabolic tangent
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
            if self.function == 1:
                o_val = 1 / (1 + math.exp(o_sum * -1))
            else:
                o_val = (math.exp(2 * o_sum) - 1) / (math.exp(2 * o_sum) + 1)
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
