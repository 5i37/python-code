time1 = int(input("enter first time in 24 houre format : "))
time2 = int(input("enter second time in 24 houre format : "))

if time1 < time2 :
    print("first time is come before second time")
elif time1 > time2 :
    print("second time is come before first time ")

else :
    m1 = int(input("enter the minte for first time :"))
    m2 = int(input("enter the minte for second time :"))
    if m1 < m2 :
        print("first time is come before second time")
    elif m1 > m2 :
        print("second time is come before first time ")