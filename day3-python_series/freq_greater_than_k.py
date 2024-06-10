l=[8,9,8,9,8,8,5,5,4,5]
print("original list:",l)
k=2
newl=[]
for i in l:
    freq=l.count(i) # this will count ex:8 how many times it came here 4 times 8 came
    if freq>2 and i not in newl:
        newl.append(i)
print("the requiered elements:",newl)