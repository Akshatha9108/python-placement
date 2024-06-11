tuple_int=(4,3,5,6,1)
sorted_t=tuple(sorted(tuple_int))
print ("sorted tuple:",sorted_t)
print("\n")
print("-------------------sorted using lamda based on alphabetical------------------------------------------------------------")
#using lambda helps to sort in single line
#based on alphabetical order
t=((1,"app"),(2,"orange"),(3,"bana"))
sort=sorted(t,key=lambda x:x[1])
print(sort)
print("\n")
print("-------------------------------tuple comprehension------------------------------------------------")
#tuple comprehension to create a tuple of squares
squre_tuple=tuple(x**2 for x in range(1,6))
print(squre_tuple)
print("\n")
print("-------------------------------Zip of tuple------------------------------------------------")
l1=[1,2,3]
l2=['a','b','c']
print(tuple(zip(l1,l2)))