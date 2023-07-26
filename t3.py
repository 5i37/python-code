import random


rand_list = [ ]

for i in range(5,100000):
    n = random.randint(5,100000)
    rand_list.append(n)
    
print (rand_list)