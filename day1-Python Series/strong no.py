#check a no. is strong or not
# The sum of factorial of individual digits is equal to the number itself -> strong number
import math
n=int(input("Enter number:"))
t=n
f=1
sum=0
while(n!=0):
    digit=n%10
    f=math.factorial(digit)
    sum+=f
    n=n//10
if t==sum:
    print("Is strong number")
else:
    print("Not strong number")

