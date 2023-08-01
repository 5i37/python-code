def calAvergae(value):
    sum=0
    num_s= int(len(value))
    averge=0
    for i in value :
        sum = sum +i
    
    averge = sum/num_s
    return averge
        





score = [76,89,90,66,82]

print(calAvergae(score))
