def area_sqr (length):
    area = length**2 
    return area

def area_cir (length) :
    import math 
    area = math.pi * (length/2)**2
    return area

def area_rect (length,width):
    area = length * width 
    return area

def area_cylinder (length,hight) :
    import math
    r = length/2
    area = (math.pi*(r)**2)+(hight*math.pi*2*r)
    return area

def area_tri (hight, base):
    area = hight * (0.5* base)
    return area


ans = 0
while ans != -1 :
    ans = int(input("please enter any number from 1-5, and enter -1 to go out from this program :"))
    
    if ans == -1 :
        break
    
    elif ans == 1 :
        area = int(input("enter the length which equal the width too : "))
        print(area_sqr(area))
        
    elif ans == 2 :
        area = int(input("enter the length : "))
        
        print(area_cir(area))
    
    elif ans == 3 :
        l = int(input("enter the length  : "))
        w = int(input("enter the width  : "))
        print(area_rect(l,w))
    
    elif ans == 4 :
        l = int(input("enter the length  : "))
        h = int(input("enter the hight  : "))
        print(area_cylinder(l,h))
        
    elif ans == 5 :
        l = int(input("enter the length which equal the width too : "))
        b = int(input("enter the base  : "))
        print(area_tri(l,b))
        
    else :
        print("plese enter correct number from 1-5 only or -1 to go out !!")