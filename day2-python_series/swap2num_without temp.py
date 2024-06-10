a=int(input())
b=int(input())

a=a+b
b=a-b
a=a-b
# 3 and 6 take a=3 b=6 then a=9 
#b=(a-b)-----> 9-6=>3
#a=(a-b)-----> 9-3=6

print("after a:",a)
print("after b:",b)