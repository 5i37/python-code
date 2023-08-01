contact = {"khalid":9298550,"ahmed":8899666,"ali":999779}

#copy dict 
new_contact = dict(contact)
# get one value from dict
print(new_contact["khalid"])
# get all keys in dict 
print(new_contact.keys())
# get all values in dict 
print(new_contact.values())

print("-"*60)
# check name in dict or not   

if "ali" in contact :
    print("yes is here ")
    
else :
    print("no not here ")
    
    
print("-"*60)
# check name in dict or not   
if "omar" in contact :  
    print("yes is here ")
    
else :
    print("no not here ")
    
    
    
# get value of contact by get method if not have will return 404    
number = contact.get("ahmed",404)
number = contact.get("said",404)
print(number)
print("-"*60)
    
# add key and value in dict
contact["julian"] = 79997
print(contact)
print("-"*60)
    
# delete one key
deleted_key = contact.pop("ali")# add it to new variable 
print(contact)
print("-"*60)
print(deleted_key)
print("-"*60)

for key in contact:
    print(key, contact[key])
    
print("-"*60)
    
for item in contact.items():
    print(item[0],item[1])
        
print("-"*60)    
    
    
    
    
    
    
    