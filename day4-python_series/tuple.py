#creating tuples
print('--------------------Creating tuples---------------------------')
def create_tuples():
    tuple1=(1,3,4,8)
    tuple2=('a','b','c')
    tuple3=("apple","banana","cherry")
    print(tuple1,tuple2,tuple3)
print("\n")
print('----------------access_tuple_items-------------------------------')
def access_tuple_items(tuple1,tuple2):
    print("tuple1:",tuple1)
print("\n")
print('----------------unpacking_tuple1-------------------------------')
def unpacking_tuple1(tuple3):
    (green,yellow,red)=tuple3
    print(green)
    print(yellow)
    print(red)
print("\n")
print('----------------unpacking_tuple2-------------------------------')
def unpacking_tuple2(fruits):
    #unpacking using asterisk
    fruits=("apple","banana","cherry","strawberry","rasberry")
    (green,yellow,*red)=fruits
    print(green)
    print(yellow)
    print(red)
print("\n")
print('----------------change_tuples-------------------------------')
def change_tuples(tuple1,tuple2):
    list1=list(tuple1)
    list2=list(tuple2)
    list1.append(6)
    list2.remove('c')
    tuple1=tuple(list1)
    tuple2=tuple(list2)
    return tuple1,tuple2
print("\n")
print('----------------change_tuples-------------------------------')
def loop_through_tuple(tuple1):
    print("looping through tuple 1 using for loop:")
    for i in tuple1:
        print(i)

    print('\nlooping using while loop and index numbers:')
    index=0
    while index<len(tuple1):
        print(tuple1[index])
        index+=1
def join_tuples(tuple1,tuple2):
    tuple3=tuple1+tuple2
    return tuple3

tuple1,tuple2,tuple3=create_tuples()
access_tuple_items(tuple1,tuple2)
print()

unpacking_tuple1(tuple3)
print()

fruits=("apple","banana","cherry","strawberry","rasberry")
unpacking_tuple2(fruits)
print()

tuple1,tuple2=change_tuples(tuple1,tuple2)
print("after making changes:")
access_tuple_items(tuple1,tuple2)
print()

tuple3=join_tuples(tuple1,tuple2)
print("join_tuples:",tuple3)