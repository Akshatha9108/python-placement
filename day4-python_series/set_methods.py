#add() method
print("-----------------Add() method---------------------")
thisset={"apple","banana","cherry"}
thisset.add("mango")
print(thisset)
print("\n")
print("-----------------Update() method---------------------")
thisset={"apple","banana","cherry"}
tropical={"pinee","mang","papa"}
thisset.update(tropical)
print(thisset)
print("\n")
print("----------------using diff types Update() method---------------------")
thisset={"apple","banana","cherry"}
mylist=["kiwi","orange"]
thisset.update(mylist)
print(thisset)
print("\n")
print("-----------------remove() method---------------------")
thisset={"apple","banana","cherry"}
thisset.remove("banana")
print(thisset)
print("\n")
print("-----------------discard() method---------------------")
thisset={"apple","banana","cherry"}
thisset.discard("banana")
print(thisset)
print("\n")
print("-----------------Pop() method---------------------")
thisset={"apple","banana","cherry"}
x=thisset.pop()
print(x)
print(thisset)
print("\n")
print("-----------------clear() method---------------------")
thisset={"apple","banana","cherry"}
thisset.clear()
print(thisset)

print("\n")
print("-----------------del--------------------")
thisset={"apple","banana","cherry"}
del thisset
print(thisset)