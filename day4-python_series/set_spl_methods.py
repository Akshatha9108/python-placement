print("-----------------Union method--------------------")
set1={"a","b","c"}
set2={1,2,3}
set3=set1.union(set2)
print(set3)

print("\n")
print("-----------------operator using union() method--------------------")
set1={"a","b","c"}
set2={1,2,3}
set3=set1|set2
print(set3)

print("\n")
print("-----------------intersection method--------------------")
set1={"apple","banana","cherry"}
set2={"google","micro","apple"}
set3=set1.intersection(set2)
print(set3)

print("\n")
print("-----------------intersection method--using operator------------------")
set1={"apple","banana","cherry"}
set2={"google","micro","apple"}
set3=set1&set2
print(set3)

print("\n")
print("-----------------intersection_update method--------------------")
set1={"apple","banana","cherry"}
set2={"google","micro","apple"}
set1.intersection_update(set2)
print(set1)

print("\n")
print("-----------------difference()update method--------------------")
set1={"apple","banana","micro"}
set2={"google","banana","apple"}
set1.difference_update(set2)
print(set1)

print("\n")
print("-----------------symmetric methods()update method--------------------")
set1={"apple","banana","micro"}
set2={"google","banana","apple"}
set1.symmetric_difference_update(set2)
print(set1)