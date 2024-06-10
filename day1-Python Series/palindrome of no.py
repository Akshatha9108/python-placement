#check if a number is palindrome or not
n=int(input("enter number"))
t=n
rev=0
while n!=0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print(rev)
if(t==rev):
    print("palindrome")
else:
    print("not palindrome")