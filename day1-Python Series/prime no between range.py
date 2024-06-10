#generate prime no. from 1 to n and count no.of prime no.s

a = int(input("Enter a number1: "))
b = int(input("Enter a number2: "))
c = 0
f=0
for i in range(a,b+1):
    if i==2:
        print(i)
        c+=1
    if i==0 or i==1:
        continue
    for j in range(2,i):
        if i%j!=0:
            f=1
        else:
            f=0
            break
    if f==1:
        print(i)
        c+=1
print("No. of prime numbers are",c)