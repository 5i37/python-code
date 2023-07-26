gender = input("enter your gender :")

gender = gender.lower()

if gender =="male":
    age = int (input("enter your age :"))
    if 24 <= age <= 30 :
        print("you are accepted")
    else :
         print ("you are rejected")
else :
    print ("your gender is not allowed")