m = [[1,2,3],
     [4,5,6]]

m2 = [[10,8,3],
     [6,4,6]]

m3=[]

if len(m)==len(m2) and len(m[0]) == len(m2[0]) and len(m[1]) == len(m2[1]):

    for i in range(2):
        for j in range(3):
              m3.append(m[i][j]+m2[i][j])
              
       
print(m3)

print(len(m[0]))