__author__ = 'Avantha'

in_out_file = open('in_outs.csv', 'r')
in_out_text = in_out_file.read()
in_out_file.close()
templist = in_out_text.split('\n')
list1 = templist[0].split(',')
list2 = templist[1].split(',')

list1 = [i for i in list1 if i != '']
list2 = [i for i in list2 if i != '']

list1 = list(map(float, list1))
list2 = list(map(float, list2))

print(list1)
print(list2)
x = 'Ads file writing...'
print(x)
x = 'ads file write completed'
print(x)
print(list1[1] + list2[2])
