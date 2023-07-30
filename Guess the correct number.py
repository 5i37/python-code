import random

num = random.randint(1,10)
print(num)

fl = False 
while not fl :
    ans = int(input("enter your answer : "))
    
    if ans > num :
        print("chose lower number : ")
    elif ans < num :
        print(" chose bigger number : ")
    else  :
        print("your answer correct, Thank you !!")
        fl = True
        