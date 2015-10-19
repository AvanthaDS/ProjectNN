__author__ = 'Avantha'

ads_neurons_n = 3

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

# define the number if input and output weights
in_n = t_in_lst[0].split(',')
ot_n = t_out_lst[0].split(',')

in_lyr_nw = ads_neurons_n * len(in_n)
out_lyr_nw = ads_neurons_n * len(ot_n)
print(in_lyr_nw)
print(out_lyr_nw)

if len(t_in_lst) != len(t_out_lst):
    print('Data mismatch, number of inputs does not match number of outputs')
else:
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
            print(list1[0])
            print(list2[0])
