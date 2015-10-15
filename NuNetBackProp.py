__author__ = 'Avantha'
import math

a = 0.35
b = 0.9
xa = 0.1
ya = 0.8
xb = 0.4
yb = 0.6
aa = 0.3
ba = 0.9
exp = 0.5
ln_rate = 1


def NuVal(v_in1, v_in2, w1, w2):
    Nuron = 1 / (1 + math.exp(((v_in1 * w1) + (v_in2 * w2)) * -1))
    return Nuron


def error(tgt, out):
    res_error = (tgt - out) * (1 - out) * out
    return res_error


def Nuerror(prevEr, prevW, out):
    NuronError = out * (1 - out) * (prevEr * prevW)
    return NuronError


def new_w(w, er, prev_out):
    w_new = w + (ln_rate * er * prev_out)
    return w_new


A = NuVal(a, b, xa, ya)
B = NuVal(a, b, xb, yb)
alpha = NuVal(A, B, aa, ba)
er1 = error(exp, alpha)
aa = new_w(aa, er1, A)
ba = new_w(ba, er1, B)
A_err = Nuerror(er1, aa, A)
B_err = Nuerror(er1, ba, B)
xa2 = new_w(xa, A_err, a)
ya2 = new_w(ya, A_err, a)
xb2 = new_w(xb, B_err, b)
yb2 = new_w(yb, B_err, b)

print('value for A:', NuVal(a, b, xa, ya))
print('Value for B:', NuVal(a, b, xb, yb))
print('value for output:', alpha)
print('Error :', er1)
print(aa, ba)
print(A_err, B_err)
print('', xa2, '\n', ya2, '\n', xb2, '\n', yb2)
