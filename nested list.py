m = [[1,2,3],
     [4,5,6]]

for i in m:
    for j in i :
        print(j, end="")
        
        
print("")        
print("-"*50)       
    
for i in range(1):
    print(m[i])
    
    for j in range(2):
        print(m[j][i])
    
        