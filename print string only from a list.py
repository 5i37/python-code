x = [1.2,3,"name"]

for i in range(len(x)) :
    if type(x[i]) == str :
        print(x[i]," is a string")
    
    else :
        print(x[i], " is not string")