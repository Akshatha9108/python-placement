# check if a no. is spy no. or not
# sum  of digits == product of digit

n=int(input("Enter no.:"))
t=n
sum=0
pro=1
while(n!=0):
    digit=n%10
    sum+=digit
    n=n//10
while(t!=0):
    digit=t%10
    pro*=digit
    t=t//10
if(sum==pro):
    print("spy number")
else:
    print("not spy number")


