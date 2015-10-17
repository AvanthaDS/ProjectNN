__author__ = 'Avantha'

listW = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
listD = [0.02, 0.03]
listV = [1, 2, 3]
brk = len(listV)
i = 0
'''while i < len(listW):
    print(listW[i:i+brk])
    i += brk
'''

for x in listV:
    k = 0
    sump = []
    for y in listD:
        aprod = y * listW[i + k]
        sump.append(aprod)
        k += brk
    print('summations:', x, sum(sump))
    # print(x,sum(sump))
    i += 1

'''for x in range(0,len(listD)):
    for y in range(0,len(listV)):
        print(listD[x],listV[y],listW[i])
        i += 1
'''
