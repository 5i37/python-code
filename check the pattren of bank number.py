card =  input("enter your CVV numer ex:xxxx-xxx : ")

if len(card) == 8 :

    if card[0:4].isdigit() and card[4] =="-" and card[5:].isdigit():
            print("yes, it's valid number ")
    else :
            print("no, it's not valid number ")
else :
    print("enter the number in correct form plese ex: xxxx-xxx")