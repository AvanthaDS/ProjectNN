__author__ = 'Avantha'
# this file need a littlebit of work

from CommonClassfn import DynamicNeuralVal
from CommonClassfn import NewWCalc
from CommonClassfn import HidnErroCalc

in_cnfg_file = open('data_cnfg/ads_train_config_data.txt', 'r')
in_cnfg_text = in_cnfg_file.read()
c_list = in_cnfg_text.split('\n')
c_list =[i for i in c_list if i != '']
c_list = list(map(float,c_list))

in_cnfg_input_n = c_list[0]
in_cnfg_output_n = c_list[1]
in_cnfg_nwrn_n = c_list[2]
in_cnfg_lnrate = c_list[5]
in_cnfg_tgt_er = c_list[6]

# -----------------------------------------------------
in_trained_w = open('data_cnfg/ads_trained weights.txt')
in_trained_text = in_trained_w.read()
in_trained_w.close()
w_list = in_trained_text.split('\n')
w_cln_list = []
for k in w_list:
    symbols = ']['
    for i in range(0, len(symbols)):
        k = k.replace(symbols[i], "")
    if len(k) > 0:
        w_cln_list.append(k)
w_list1 = w_cln_list[0]
w_list1 = w_list1.split(',')
w_list1 = list(map(float, w_list1))
w_list2 = w_cln_list[1]
w_list2 = w_list2.split(',')
w_list2 = list(map(float, w_list2))

file_inputs = open('data_validate/validate_in.csv', 'r')
text_t_in = file_inputs.read()
file_inputs.close()
file_outputs = open('data_validate/validate_out.csv', 'r')
text_t_out = file_outputs.read()
file_outputs.close()

t_in_lst = text_t_in.split('\n')
t_in_lst = [i for i in t_in_lst if i != '']

t_out_lst = text_t_out.split('\n')
t_out_lst = [i for i in t_out_lst if i != '']

ads_neurons_n = in_cnfg_nwrn_n
ads_lrn_rate = in_cnfg_lnrate
ads_itn_n = 1
ads_itn_cntr = 1
ads_in_ws = w_list1
ads_out_ws = w_list2
ads_abs_error_stat = []
ads_abs_error =[]

if len(t_in_lst) != len(t_out_lst):
    print('Data mismatch, number of inputs does not match number of outputs')
    ads_abs_error_stat.append('Validation I/O data mismatch')
else:
    while ads_itn_cntr >=in_cnfg_tgt_er:
        ads_temp_err2 = []
        for n in range(0, len(t_in_lst)):
            list1 = t_in_lst[n].split(',')
            list2 = t_out_lst[n].split(',')
            list1 = [i for i in list1 if i != '']  # remove null values
            list2 = [i for i in list2 if i != '']
            list1 = list(map(float, list1))  # convert string to float so that calculations can take place
            list2 = list(map(float, list2))
            ads_input_vals = list1
            ads_target_vals = list2

            # check if the input values number in training matches the validation input numbers
            if len(ads_input_vals) == in_cnfg_input_n and len(ads_target_vals) == in_cnfg_output_n:

                # forward pass 1st iteration C1 - <class><number>
                # pass the inputs to the neuron calc class
                ads_C1 = DynamicNeuralVal(ads_input_vals, ads_neurons_n, ads_target_vals, ads_in_ws, ads_out_ws)
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

                ads_temp_err1 = []

                for i in ads_out_errs:
                    ads_temp_err1.append(abs(i))
                ads_temp_err2.append(sum(ads_temp_err1))
                ads_chk = sum(ads_temp_err1)
                del ads_temp_err1[:]

                if ads_chk > in_cnfg_tgt_er:
                    ads_in_ws = ads_new_inw
                    ads_out_ws = ads_new_ow



        ads_abs_error.append(sum(ads_temp_err2))
        del ads_temp_err2[:]

        ads_itn_cntr = ads_abs_error[-1]
        print(ads_itn_cntr)



ads_refined_w = 'data_cnfg/refined_weights.txt'
refined_w_file = open(ads_refined_w, 'w')
refined_w_file.write(str(ads_in_ws) + '\n')
refined_w_file.write(str(ads_out_ws))
refined_w_file.close()
print('Report generation complete')
