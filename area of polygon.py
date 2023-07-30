def area(n,side):
    import math
    area = (n*(side**2))/ (4*(math.tan((math.pi)/(n))))
    
    return area


num_of_side= int(input("enter number of sildes :"))
side= float(input("enter the side :"))

polygon = area(num_of_side,side)

print("the area of the polygon is : ",polygon)