l=[9,4,4,3,2,3]
count=0
un=[]
for i in l:
    if i not in un:
        count+=1
        un.append(i)


print(un)
print(count)