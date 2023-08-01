from sympy import *


for i in range(1,31):
    
    if i == 1 :
        print(i,"","","|","True")
    else :
        print(i,"","","|",isprime(i))

