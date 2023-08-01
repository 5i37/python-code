li = [10,20,30,90]
pos= 0
limit = 90
flg = False
while pos < limit and not flg :
    if li[pos] == 90 :
        flg = True
    else :
        pos +=1
    
if flg :
    print("the number in postion",pos)

else :
        print("the number not found in this list",pos)
