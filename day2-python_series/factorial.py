n=int(input())
fact=1
if n<0:
    print("does not exit")
elif n==0:
    print("fact is 1")
else:
    for i in range(1,n+1):
        fact=fact*i
    print("The factorial of ",n,"is",fact)