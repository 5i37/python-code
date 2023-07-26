#Calculate Your Body Mass Index

weight = float (input("enter your weight in  Kg :"))
height = float (input("enter your height in Cm :"))

height = height/100
BMI = weight / (height)**2

if BMI <18.5:
    print("UnderWeight ")
elif 18.5 <= BMI <25.0:
    print("Normal")
elif 25.0 <= BMI <30.0:
    print("OverWeight")
else :
    print("Obese")
    
    
    
#Done by: khalid alrashdi 