


for n in range(1,101):
    sm  = 0
    for  i in range(1,n):
        if n%i == 0 :
            sm+=i
    if n == sm :
        print (n, "is a perfect number")
            