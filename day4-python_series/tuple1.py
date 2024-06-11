my_tuple=(1,2,3)
another=tuple([4,5,6])
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:3])
combine=my_tuple+another
print(combine)
repeated_tuple=my_tuple*3
print(repeated_tuple)
print(2 in my_tuple) #o/p is True
print(4 not in my_tuple)
print(len(my_tuple))
for i in my_tuple:
    print(i)
string_to_tuple=tuple("hello")
print("string to tuples:",string_to_tuple)
list_to_tuple=tuple([1,2,3])
print("list_to_tuple:",list_to_tuple)
print(my_tuple.count(2)) #outpu 1
print(my_tuple.index(3)) #outpu 2