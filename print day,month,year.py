def rdate():
    month = int (input("enter month :"))
    day = int (input("enter day :"))
    year = int (input("enter year :"))
    
    return (month,day,year)

date = rdate()
print(date)

(month,day,year)=rdate()
print(month,day,year)
