#check if a no. armstrong or not
#a number whose sum of digits power no. of digits is same as original number

ans=0
strnum=input("enter no.:")
size=len(strnum)
n=int(strnum)
t=n
while(n!=0):
    digit=n%10
    ans+=digit**size
    n=n//10
if(ans==t):
    print("Is Armstrong number")
else:
    print("Not Armstrong no. ")


