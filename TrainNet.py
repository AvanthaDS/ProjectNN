__author__ = 'Avantha'
import random

from CommonClassfn import DynamicNeuralVal
from CommonClassfn import NewWCalc
from CommonClassfn import HidnErroCalc

# user inputs !!! Makesure the same function is not called twice this will create more lists !!!!
in_out_file = open('train_in_outs.csv', 'r')
in_out_text = in_out_file.read()  # read the input file and assign to text
f_list = in_out_text.split('\n')  # break the two line to input and output
in_out_file.close()
list1 = f_list[0].split(',')  # split the values using the ','
list2 = f_list[1].split(',')
list1 = [i for i in list1 if i != '']  # remove null values
list2 = [i for i in list2 if i != '']
list1 = list(map(float, list1))  # convert string to float so that calculations can take place
list2 = list(map(float, list2))
ads_input_vals = list1
ads_target_vals = list2


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

    ads_tmp_err = []
    for x in ads_out_errs:
        ads_tmp_err.append(abs(x))
    ads_abs_error.append(sum(ads_tmp_err))
    del ads_tmp_err[:]

    ads_in_ws = ads_new_inw
    ads_out_ws = ads_new_ow

    ads_itn_cntr += 1


print('calculation complete')
# -----------------------------------
# Creating the weights file
ads_w_file = 'ads_trained weights.txt'
w_file = open(ads_w_file, 'w')
w_file.write(str(ads_in_ws) + '\n')
w_file.write(str(ads_out_ws) + '\n')
w_file.close()
print('w file write complete')

# creating the error reduction file
start_err = ads_abs_error[0]
end_err = ads_abs_error[-1]
print(start_err)
print(end_err)
ads_file = 'Ads_Err_Reduction.csv'
fx = open(ads_file, 'w')
for x in ads_abs_error:
    fx.write(str(x) + '\n')
fx.close()
print('Abs Error file write complete')

# Creating setup information
ads_config_file = 'ads_train_config_data.txt'
w_config = open(ads_config_file, 'w')
w_config.write(str(len(ads_input_vals)) + '\n')
w_config.write(str(len(ads_target_vals)) + '\n')
w_config.write(str(ads_neurons_n) + '\n')
w_config.write(str(len(ads_in_ws)) + '\n')
w_config.write(str(len(ads_out_ws)) + '\n')
w_config.write(str(ads_lrn_rate)+'\n')
w_config.close()
print('Config file write complete')
