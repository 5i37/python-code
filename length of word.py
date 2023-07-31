x = ['red', 'yellow', 'pink', 'black']

n = int(input("enter the length : "))
for i in x :
    word = str(i)
    if int (len(word))>n :
        print(word)