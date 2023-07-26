integer =int(input("enter any number : "))
output = [int(x) for x in str(integer)]

if output[0] == output[-1]:
    
    print("Ture, is a palindrome")
else :
    print("fulse, isn't a palindrome")