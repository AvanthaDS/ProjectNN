__author__ = 'Avantha'
import math
i =0
A =[]
B =[]
xa =[]
ya =[]
xb =[]
yb =[]
aa =[]
ba =[]
alpha =[]
a = 0.35
b = 0.9
xa.append(0.1)
ya.append(0.8)
xb.append(0.4)
yb.append(0.6)
aa.append(0.3)
ba.append(0.9)
exp = 0.5
ln_rate = 1
er=[]
A_err =[]
B_err =[]

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
    print(er[i])
    #print(aa[i+1], ba[i+1])
    #print(A_err[i], B_err[i])
    #print('', xa[i+1], '\n', ya[i+1], '\n', xb[i+1], '\n', yb[i+1])

    i += 1

