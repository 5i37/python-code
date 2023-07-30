
letter = input("enter the first number :")
letter = letter.lower()
counter = 0
l = []
for i in letter :
    if i == "a" :
        counter+=1
        l.append(i)
    elif i == "i" :
        counter+=1
        l.append(i)
    elif i == "o" :
        counter+=1
        l.append(i)
    elif i == "u" :
        counter+=1
        l.append(i)
    elif i == "e" :
        counter+=1
        l.append(i)
        
print("number of letter vowels are : ", counter)
print("which are : ",l)