def power(n,p):
    if p == 1:
       return n
    elif p%2!=0:
        temp=pow(n,p//2)
        return n*temp*temp
    else:
        temp=pow(n,p//2)
        return temp*temp
n=2
p=5
print(power(n,p))
