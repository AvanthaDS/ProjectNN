__author__ = 'Avantha'

from CommonClassfn import DynamicNeuralVal

# user inputs !!! Makesure the same function is not called twice this will create more lists !!!!
in_out_file = open('validate.csv', 'r')
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

in_cnfg_file = open('ads_train_config_data.txt','r')
in_cnfg_text = in_cnfg_file.read()
c_list = in_cnfg_text.split('\n')
c_list =[i for i in c_list if i != '']
c_list = list(map(float,c_list))

in_cnfg_input_n = c_list[0]
in_cnfg_output_n = c_list[1]
in_cnfg_nwrn_n = c_list[2]
in_cnfg_inw_n = c_list[3]
in_cnfg_outw_n = c_list[4]
in_cnfg_lnrate = c_list[5]
in_cnfg_tgt_er = c_list[6]

in_trained_w = open('ads_trained weights.txt')
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

ads_neurons_n = in_cnfg_nwrn_n
ads_lrn_rate = in_cnfg_lnrate
ads_itn_n = 1
ads_itn_cntr = 1
ads_in_ws = w_list1
ads_out_ws = w_list2
ads_abs_error = []

# check if the input values number in training matches the validation input numbers
if len(ads_input_vals) == in_cnfg_input_n and len(ads_target_vals) == in_cnfg_output_n:
    ads_v1 = DynamicNeuralVal(ads_input_vals,in_cnfg_nwrn_n,ads_target_vals,ads_in_ws,ads_out_ws)
    ads_v1.dum_n_cal()
    ads_v1.dum_out_cal()
    ads_validate_er = ads_v1.dum_o_error()
    print('output errors:', ads_validate_er)
    for i in ads_validate_er:
        ads_abs_error.append(abs(i))
    print('Absolute combined error:', sum(ads_abs_error))
    if in_cnfg_tgt_er > sum(ads_abs_error):
        print('Validation PASS !!')
    else:
        print('Validation FAIL !!!')
else:
    print('Validation inputs does not match training inputs !')
