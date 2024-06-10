#test if list containig element in range
'''
l=[1,3,2,3,5,8]
for i in range(2,10):
    if i in l:
        print(i)
print("not present")
'''
l=[4,5,6,7,3,9,12]
i,j=3,9
res=True
for x in l:
    if x<i or x>j:
        res=False
        break
print("Does list contain all elements in range",res)