from math import *

lenth = 4
hight = 5
s_try = hight * (0.5* lenth)
s_sqr = lenth  * lenth
s_circ = pi * (lenth/2)**2

area = (s_try + s_sqr) - s_circ

print(area)