# generate the fibonacci series and fibonocci no.of a given no.
n=int(input("enter range:"))
f0=0
f1=1
if n==1:
    print(f0,end=" ")
    exit
if n==2:
    print(f0,end=" ")
    print(f1,end=" ")
    exit
print(f0,end=" ")
print(f1,end=" ")
for i in range(n):
    f2=f0+f1
    f0=f1
    f1=f2
    print(f2,end=" ")
