print("Number","|","Prime Status")
print("-"*22)

# If given number is greater than 1
for x in range(1,31):
    if x > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(x/2)+1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (x % i) == 0:
                print(x,"","","|","False")
                break
        else:
            print(x,"","","|","True")
    else:
        print(x,"","","|","False")
