__author__ = 'Avantha'
import random

from CommonClassfn import DynamicNeuralVal
from CommonClassfn import NewWCalc
from CommonClassfn import HidnErroCalc

ads_neurons_n = 10  # number of Neurons required - Fix
ads_lrn_rate = 1  # enter learning rate - Fix
ads_itn_n = 4  # number of iterations required
ads_itn_cntr = 1  # do not change manually
ads_tgt_error = 0.01
ads_function = 1  # 1 - Sigmoid , 2 - Hypabolic tangent must trouble shoot the Htanjent issue( it dows not reduce)
ads_in_ws = []
ads_out_ws = []
ads_abs_error = []
ads_numberof_itn = 1

# user inputs !!! Makesure the same function is not called twice this will create more lists !!!!
file_inputs = open('data_train/train_inputs.csv', 'r')
text_t_in = file_inputs.read()
file_inputs.close()
file_outputs = open('data_train/train_outputs.csv', 'r')
text_t_out = file_outputs.read()
file_outputs.close()

t_in_lst = text_t_in.split('\n')
t_in_lst = [i for i in t_in_lst if i != '']

t_out_lst = text_t_out.split('\n')
t_out_lst = [i for i in t_out_lst if i != '']

# ----------define the number if input and output weights--------
in_n = t_in_lst[0].split(',')
ot_n = t_out_lst[0].split(',')

in_lyr_nw = ads_neurons_n * len(in_n)
out_lyr_nw = ads_neurons_n * len(ot_n)

i = 1
j = 1
while i <= in_lyr_nw:
    ads_in_ws.append(round(random.random(), 3))
    i += 1
while j <= out_lyr_nw:
    ads_out_ws.append(round(random.random(), 3))
    j += 1
# ---------------------------------------------------


if len(t_in_lst) != len(t_out_lst):
    print('Data mismatch, number of inputs does not match number of outputs')
else:
    while ads_itn_cntr >= ads_tgt_error:
        ads_temp_err2 = []  # temp error to store the absolute data list error to write to the file
        for n in range(0, len(t_in_lst)):
            list1 = t_in_lst[n].split(',')
            list2 = t_out_lst[n].split(',')
            list1 = [i for i in list1 if i != '']  # remove null values
            list2 = [i for i in list2 if i != '']
            list1 = list(map(float, list1))  # convert string to float so that calculations can take place
            list2 = list(map(float, list2))
            if len(list1) != len(in_n) or len(list2) != len(ot_n):
                print('Data mismatch, one or many inputs/out puts has missing data')
            else:
                ads_input_vals = list1
                ads_target_vals = list2


                # forward pass 1st iteration C1 - <class><number>
                # pass the inputs to the neuron calc class
                ads_C1 = DynamicNeuralVal(ads_input_vals, ads_neurons_n, ads_target_vals, ads_in_ws, ads_out_ws,
                                          ads_function)
                ads_nvals = ads_C1.dum_n_cal()
                ads_outvals = ads_C1.dum_out_cal()
                ads_out_errs = ads_C1.dum_o_error()


                # back propagation output layer weights correction
                ads_output_ws = ads_C1.ouw
                ads_C2 = NewWCalc(ads_output_ws, ads_out_errs, ads_nvals, ads_lrn_rate)
                ads_new_ow = ads_C2.dum_w_new()


                # Back propagation hidden layer error calculation
                ads_C3 = HidnErroCalc(ads_nvals, ads_new_ow, ads_out_errs)
                ads_hdnl_errs = ads_C3.out_errors()

                # back propagation input layer weights correction
                ads_input_ws = ads_C1.inw
                ads_C4 = NewWCalc(ads_input_ws, ads_hdnl_errs, ads_input_vals, ads_lrn_rate)
                ads_new_inw = ads_C4.dum_w_new()

                ads_in_ws = ads_new_inw
                ads_out_ws = ads_new_ow

                ads_temp_err1 = []
                for i in ads_out_errs:
                    ads_temp_err1.append(abs(i))
                ads_temp_err2.append(sum(ads_temp_err1))
                del ads_temp_err1[:]

        #ads_abs_error.append(sum(ads_temp_err2) / len(ads_temp_err2)) # THis will not pass all in the validation
        ads_abs_error.append(sum(ads_temp_err2))

        del ads_temp_err2[:]

        ads_numberof_itn += 1
        ads_itn_cntr = ads_abs_error[-1]
        # print(ads_abs_error[-1])


print('calculation complete')
print('Number of iterations performed:', ads_numberof_itn)
# -----------------------------------
# Creating the weights file
ads_w_file = 'data_cnfg/ads_trained weights.txt'
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
ads_file = 'analysis/Ads_Err_Reduction.csv'
fx = open(ads_file, 'w')
for x in ads_abs_error:
    fx.write(str(x) + '\n')
fx.close()
print('Abs Error file write complete')

# Creating setup information
ads_config_file = 'data_cnfg/ads_train_config_data.txt'
w_config = open(ads_config_file, 'w')
w_config.write(str(len(in_n)) + '\n')
w_config.write(str(len(ot_n)) + '\n')
w_config.write(str(ads_neurons_n) + '\n')
w_config.write(str(len(ads_in_ws)) + '\n')
w_config.write(str(len(ads_out_ws)) + '\n')
w_config.write(str(ads_lrn_rate)+'\n')
w_config.write(str(ads_tgt_error) + '\n')
w_config.write(str(ads_function))
w_config.close()
print('Config file write complete')
