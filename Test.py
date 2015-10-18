__author__ = 'Avantha'

file = open('in_outs.csv', 'r')
text = file.read()

f = text.split('\n')

print(text)
print(f[0])
print(f[1])

list1 = f[0].split(',')
list2 = f[1].split(',')

print(list1)
print(list2)

print(len(list1))
print(len(list2))

x = float(list1[0]) + float(list2[2])
print(x)

file.close()
