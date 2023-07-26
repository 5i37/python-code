unit = int(input("enter units : "))
bill = 0
if unit <= 100:
    print("No charges")
    
elif 100<unit <=200:
    bill = unit * 0.024
    print("your charge is : ",bill, "OMR")
else :
    bill = unit * 0.047
    print("your charge is : ",bill, "OMR")
