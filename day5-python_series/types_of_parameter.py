print("---------------------------------default Arguments--------------------------------------")
#default arguments
def myfun(x,y=50):
    print("x: ",x)
    print("y: ",y)
myfun(10) # in function call actual para not passed then it assigned default paramater directly y=50 directly

print("------------------------------Keyword Arguments-----------------------------------------")
#keyword arguments
def student(firstname,lastname):
    print(firstname,lastname)

student(firstname="akshu",lastname="snow")
student(lastname="snow",firstname="akshu") #it can not change the order

print("------------------------------Non Keyword varieable length Arguments-----------------------------------------")
#using args-non keyworded variable length arguments
def myfun1(*argv):
    print(argv)
#DRIVER CODE
myfun1("Hello","welcome",'to',"India")
print("------------------------------keyworded variable length Arguments-----------------------------------------")
#USING kwargs
def printKwargs(**kwargs):
    print(kwargs)
printKwargs(a="Hello",b="World")

print("------------------------------anonymous function-----------------------------------------")
def cube(x):
    return x*x*x
cube_v2=lambda x:x*x*x

print(cube(7))
print(cube_v2(7))
