dec = {1:{'name':'Jone','age':27,'sex':'male'},
       2:{'name':'Marie','age':22,'sex':'fmale'},
       3:{'name':'Sali','age':23,'sex':'fmale'}}


print("-"*60)

for item in dec.items() :
    if item[1]["age"] >22:
        print(item[1]["name"])
        
print("-"*60)

if dec[3]["age"]<dec[1]["age"] >dec[2]["age"]:
    print(dec[1]["name"])
        
elif dec[3]["age"]<dec[2]["age"] >dec[3]["age"]:
    print(dec[2]["name"])
        
elif dec[1]["age"]<dec[3]["age"] >dec[2]["age"]:
    print(dec[3]["name"])
        
print("-"*60)
new = dict(sorted(dec.items(), key=lambda item:item[1]["age"]))
print(new)
print("-"*60)

for item in new.items() :
    print(item[1]["name"])
        
        