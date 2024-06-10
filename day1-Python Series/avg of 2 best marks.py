#to find the best of 2 test average marks out of 3 test marks accepted from user

#given 3 marks take average of 2 best marks

a=int(input("Enter mark1:"))
b=int(input("Enter mark2:"))
c=int(input("Enter mark3:"))
if a>b and a>c:
    if b>c:
        print("Best marks are",a,"and",b,"|| Avg:",(a+b)/2)
    else:
        print("Best marks are",a,"and",c,"|| Avg:",(a+c)/2)
elif b>a and b>c:
    if a>c:
        print("Best marks are",a,"and",b,"|| Avg:",(a+b)/2)
    else:
        print("Best marks are",b,"and",c,"|| Avg:",(b+c)/2)
else:
    if a>b:
        print("Best marks are",a,"and",c,"|| Avg:",(a+c)/2)
    else:
        print("Best marks are",b,"and",c,"|| Avg:",(b+c)/2)

# or 

# x=(a+b)/2
# y=(a+c)/2
# z=(b+c)/2
# print(max(x,y,z))