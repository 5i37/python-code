n=input("enter your number : ")
m=int(n)
s=0
q=m
while(m!=0):
    p=m%10
    s+=p**(len(n))
    m=m//10
if(s==q):
    print("Yes, it's Narcissistic number")
else:
    print("No, it's Not Narcissistic number")
