l1=list(("Apple"))
l2=list(("Apple","Hat"))
print(l1)
print(l2)
print("---------------------------------------------")
l3=['a','b','c']
l4=[10,30,40,50,60]
l5=[True,False]
print(l3)
print(14)
print(l5)
print("Slicing---------------------------------------------")
print(l4[0])
print(l4[0:4])
print(l4[:4])
print(l4[0:])
print(l4[:])
#starting index should be less than or equal to valid index
print(l4[-4:-1])
print(l4[-1:-4])
x=len(l4)
print(x)
print(type(l4))
print(type(l4[0]))
if "a" in l3:
    print("exists")
print("----------------------------------replace---------------------------------------------")
l3[1]="kiwi"
print(l3)
l3[1:3]=["pinne","dates","mango"]
print(l3)
print("If you want more items")
list=["apple","banana","cherry"]
list[1:2]=["blackcuurennt","mango"]
print(list)
print("----------------------------------")
print("------------If you want less items---------------")
list[1:3]=["waterlemon"]
print(list)
print("----------------------------------")
print("\n")
print("-----------insert()-----------method insert an items at the spedific---------")
list.insert(2,"mango")
print(list)
print("\n")
print("-----------append()-----------method apppend an items at the end---------")
list.append("orange")
print(list)
print("\n")
print("-----------extend()-----------to append elements from another list to the current list---------")
list1=["app","banana","cherry"]
list2=["man","water","lemon"]
list1.extend(list2)
print(list1)
print("\n")
print("-----------pop()-----------method remove the specific index---------")
list1.pop(1)
print(list1)
print("\n")
print("-----------Remove()-----------method remove the specific value---------")
list1.remove("water")
print(list1)

print("\n")
print("-----------del---not a method  is keyword also remove the specific index---------")
print("before",list2)
del  list2[0]
print("After",list2)

print("\n")
list2=["man","water","lemon"]
print("-----------del---not a method  is keyword also remove the sentire list---------")
del  list2

print("\n")
list2=["man","water","lemon"]
print("-----------clear---method   remove the entire list---------")
list2.clear()
print(list2)


print("\n")
print("-----------for loop---------")
for x in list:
    print(x)

print("\n")
print("-----------for loop in range---------")
for i in range(0,len(list)):
    print(list[i])

print("\n")
print("-----------for loop in range in condition---------")
for i in range(0,len(list)):
    if list[i]=="apple":
        print(list[i])

    

print("\n")
print("-----------while loop---------")
i=0
while i<len(list):
    print(list[i])
    i=i+1

print("\n")
print("-------List comprehension offers the shortest syntex---------")
print("-------newList [expression for item in iterable ]--------")

[print(x) for x in list]

print("\n")
print("-----------based on list of fruist ,u want a new list containig a--------")
fruits=['apple','banana','cherry','kiwi']
newlist=[]

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

print("\n")
print("-----------using list comprehension---------")
print("-----------Newlist=[expression for item in iterable condition---------")
newlist=[x for x in fruits if "a" in x]
print(newlist)

print("\n")
print("-----------sort the list alphabets---------")
fruit=['cherry','apple','banana','kiwi','dates']
fruit.sort()
print(fruit)

print("\n")
print("-----------sort the list numerically---------")
lt=[50,80,30,20,70]
lt.sort()
print(lt)

print("\n")
print("-----------sort the list reverse---------")
lt=[50,80,30,20,70]
lt.sort(reverse=True)
print(lt)
print("\n")

print("-----------sort the list alphabets in reverse order---------")
fruit=['cherry','apple','banana','kiwi','dates']
fruit.sort(reverse=True)
print(fruit)

print("\n")
print("-----------costumised sort--------")
print('----------#sorted based on how close a number is 50---------')
def fun(n):
    return abs(n-50)
thislist=[100,50,65,82,23]
thislist.sort(key=fun)# fun is not function call simply passing function name as parameter
print(thislist)

print("\n")
print("-----------#case insensitive without giving condition capital letter as priority--------")

thislist=['cherry','apple','Banana','kiwi','dates']
thislist.sort()# if u didnot mention caseinsensitive it is priority of capital letter so we need to use lower function
print(thislist)

print("\n")
print("-----------#case insensitive--------")

thislist=['cherry','apple','Banana','kiwi','dates']
thislist.sort(key=str.lower)
print(thislist)

print("\n")
print("-----------Swap first and last element--------")
#PGM to swap first and last element of the list
def swaplist(thislist):
    n=len(thislist)
    temp=thislist[0]
    thislist[0]=thislist[n-1]
    thislist[n-1]=temp
    return thislist
thislist=[10,40,50,30]
print("before:",thislist)
print(swaplist(thislist))

print("\n")
print("-----------Swap positions--------")
def swapposition(thislist,pos1,pos2):
    temp=thislist[pos1]
    thislist[pos1]=thislist[pos2]
    thislist[pos2]=temp
    return thislist
thislist=[60,45,50,30]
pos1,pos2=1,3 #not index direct 1 2 3 4 
print(swapposition(thislist,pos1-1,pos2-1))# pos1-1vmeans converting index like 0 1 2 3 4
print('-------------------------------------------')
print("\n")
print("-----------Sum and avg in list--------")
l=[4,5,1,2,9,7,10,8]
sum=0
for i in l:
    sum=sum+i #0+4=4+5=9+1=10.......
avg=sum/len(l)

print("sum=",sum)
print("avg=",avg)
#print first and last element in list
n=len(l)
print("first element=",l[0],"\nlast element=",l[n-1])
# min and max element
l.sort()
n=len(l)
print(l[0])
print(l[n-1])