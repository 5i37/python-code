print("Number","|","Prime Status")
print("-"*22)


for i in  range(1,31):
    if i ==1 :
        print(i,"","","|","False")

    elif i ==2 or i ==3:
        print(i,"","","|","True")

    elif i % 2 == 0 :
        print(i,"","","|","False")
        
    elif i % 3 == 0 :
        print(i,"","","|","False")
    else :
        print(i,"","","|","True")
        
