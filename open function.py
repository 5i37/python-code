input_file = open("input.txt","r")


print(input_file)

for line in input_file:
    #print(line)
    print(line[0].rsplit())
    
    
    
    
    
for line in input_file:
    v= line.rsplit()
    print(v)#  split every number 