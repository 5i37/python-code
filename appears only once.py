def aur_once(num):
    for i in range(len(num)) :
        cunt = num.count(num[i])
        if cunt <2 :
            print(num[i]," is appears only once")


li = [2,2,1]

li2 = [4,1,2,1,2]

aur_once(li)

print("-"*50)

aur_once(li2)
