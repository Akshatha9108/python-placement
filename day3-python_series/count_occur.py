def count_occ(l,x):
    c=0
    for i in range(len(l)):
        if l[i]==x:
            c+=1
    return c

l=[90,40,40,30,20]
x=40
print(count_occ(l,x))