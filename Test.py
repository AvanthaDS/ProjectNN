__author__ = 'Avantha'
import math

a = 2

res1 = 1 / (1 + math.exp(a * -1))
print(res1)

res2 = (math.exp(2 * a) - 1) / (math.exp(2 * a) + 1)
print(res2)
