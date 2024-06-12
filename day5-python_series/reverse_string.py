def reverse_String(s):
    i=len(s)
    rstr=''
    while(i>0):
        rstr=rstr+s[i-1]
        i=i-1
    return rstr
str=input("enter a string to reverse:")
reverse=reverse_String(str)
print("Reversed String:",reverse)