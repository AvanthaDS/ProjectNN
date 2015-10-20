__author__ = 'Avantha'

from CommonClassfn import DynamicNeuralVal

in_cnfg_file = open('data_cnfg/ads_train_config_data.txt', 'r')
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

file_inputs = open('data_predict/predict_inputs.csv', 'r')
text_t_in = file_inputs.read()
file_inputs.close()

t_in_lst = text_t_in.split('\n')
t_in_lst = [i for i in t_in_lst if i != '']

ads_neurons_n = in_cnfg_nwrn_n
ads_lrn_rate = in_cnfg_lnrate
ads_itn_n = 1
ads_itn_cntr = 1
ads_in_ws = w_list1
ads_out_ws = w_list2
ads_target_vals =[]
ads_prediction =[]

for n in range(0, len(t_in_lst)):
    list1 = t_in_lst[n].split(',')
    list1 = [i for i in list1 if i != '']  # remove null values
    list1 = list(map(float, list1))  # convert string to float so that calculations can take place
    ads_input_vals = list1

    if len(ads_input_vals) == in_cnfg_input_n:
        ads_v1 = DynamicNeuralVal(ads_input_vals, in_cnfg_nwrn_n, ads_target_vals, ads_in_ws, ads_out_ws)
        ads_v1.dum_n_cal()
        ads_target=ads_v1.dum_out_cal()
        ads_prediction.append(ads_target)
    else:
        print('Data mismatch with training data')

ads_predict_rep = 'data_predict/Prediction_report.txt'
report_file = open(ads_predict_rep, 'w')
for i in range(0, len(ads_prediction)):
    report_file.write('Pattern:' + str(i + 1) + '-' + str(ads_prediction[i]) + '\n')

report_file.close()
print('Report generation complete')