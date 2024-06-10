def ishappy(n):
    sum=0
    while(n!=0):
        r=n%10
        sum=sum+r**2
        n=n//10
    return sum
n=int(input())
res=n
while(res!=1 and res!=4):
    res=ishappy(res)
if (res==1):
    print( "true")
elif (res==4):
    print( "false")