__author__ = 'Avantha'

tst = open('data_train/train_inputs.csv','r')
text = tst.read()
tst.close()
lst = text.split('\n')
lst= [i for i in lst if i != '']
lst = list(map(float, lst))
print(lst)



