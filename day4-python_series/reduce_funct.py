from functools import reduce
def add(a,b):
    return a+b

t=(1,2,3,4,5)
result=reduce(add,t)
print("Result of reducing tuple:",result)