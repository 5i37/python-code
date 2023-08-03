inputok = False

while (inputok==False):
    try :
        num = input("enter number :")
        num = float(num)
        inputok = True
    except ValueError:
        print("Non-numeric type entered '%s'"%num)

num = num*2
print(num)