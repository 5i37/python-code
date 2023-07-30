def bigger_num (n1,n2=10,n3=5):
    print(n3)
    if n2< n1 >n3:
        print(n1,"is the bigger number")
        
    elif n1< n2 >n3:  
        print(n2,"is the bigger number")
        
    elif n1< n3 >n2:   
        print(n3,"is the bigger number")
    else :
        print("no one bigger")
        
        
        
num1=int(input("enter first number :"))
print("--------------------------------------")
num2=int(input("enter second number :"))
print("--------------------------------------")
num3=int(input("enter third number :"))
print("--------------------------------------")

bigger_num(num1,num2)