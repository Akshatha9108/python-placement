#write a program to check if a number is prime or not

flag=0
n=int(input("Enter a number:"))
for i in range(2,n):
    if n%i==0:
        flag=1
        break
    else:
        flag=0
if(flag==1):
    print("not prime")
else:
    print("prime")

# -----------------------------------------------------------------------------