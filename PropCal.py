__author__ = 'Avantha'
import math

i = 0  # counter
A = []  # Nuron 1
B = []  # Nuron 2
xa = []  # input x to Nuron A weight
ya = []  # input y to Nuron A weight
xb = []  # input x to Nuron B weight
yb = []  # input y to Nuron B weight
aa = []  # Nuron A to output Weight
ba = []  # Nuron B to output weight
alpha = []  # output
a = 0.35  # input 1
b = 0.9  # unpit 2
xa.append(0.1)  # random weight
ya.append(0.8)  # random weight
xb.append(0.4)  # random weight
yb.append(0.6)  # random weight
aa.append(0.3)  # random weight
ba.append(0.9)  # random weight
exp = 0.5  # expected output
ln_rate = 1  # Learning rate
er = []  # error
A_err = []  # Nuron A error
B_err = []  # Nuron B error

def NuralVal(v_in1, v_in2, w1, w2):
    Nuron = 1 / (1 + math.exp(((v_in1 * w1) + (v_in2 * w2)) * -1))
    return Nuron


def error_out(tgt, out):
    res_error = (tgt - out) * (1 - out) * out
    return res_error


def error_nuron(prevEr, prevW, out):
    NuronError = out * (1 - out) * (prevEr * prevW)
    return NuronError


def new_w(w, er, prev_out):
    w_new = w + (ln_rate * er * prev_out)
    return w_new

while  i<=100:
    A.append(NuralVal(a, b, xa[i], ya[i]))
    B.append(NuralVal(a, b, xb[i], yb[i]))
    alpha.append(NuralVal(A[i], B[i], aa[i], ba[i]))
    er.append(error_out(exp, alpha[i]))
    aa.append(new_w(aa[i], er[i], A[i]))
    ba.append(new_w(ba[i], er[i], B[i]))
    A_err.append(error_nuron(er[i], aa[i+1], A[i]))
    B_err.append(error_nuron(er[i], ba[i+1], B[i]))
    xa.append(new_w(xa[i], A_err[i], a))
    ya.append(new_w(ya[i], A_err[i], a))
    xb.append(new_w(xb[i], B_err[i], b))
    yb.append(new_w(yb[i], B_err[i], b))

    #print('A is :',A[i])
    #print('B is :',B[i])
    #print('value for output:', alpha[i])
    print('Error:', er[i], 'Output:', alpha[i])

    #print(aa[i+1], ba[i+1])
    #print(A_err[i], B_err[i])
    #print('', xa[i+1], '\n', ya[i+1], '\n', xb[i+1], '\n', yb[i+1])

    i += 1

