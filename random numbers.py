import random


counter= 1
bre = 0
while  counter == 1:
    x = random.randint(1,100)
    y = random.randint(1,100)
    print (x," + ",y," = ? ")
    ans  = input("your answer :")
    
    if not (ans == "done"):
    
        if ans == str(x+y) :
            print("your answer is correct !!")
            print("-------------------------------")
        else :
             print("Sorry, your answer is not correct !!")
             print("-------------------------------")
             
       
    
    else :
        break 
