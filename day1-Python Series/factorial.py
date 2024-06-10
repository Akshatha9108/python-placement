#find factorial

# import math
# n=int(input("Enter number:"))
# print(math.factorial(n))

# or

f=1
n=int(input("Enter number:"))
if n<0:
    print("Invalid")
    exit(0)
for i in range(1,n+1):
    f*=i
print(f)
