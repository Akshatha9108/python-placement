def sum_x(a,n,x):
    for i in range(0,n):
        for j in range(1,n):
            if (i!=j and a[i]+a[j]==x):
                return True
    return False
arr=[1,-1,2,4,8]
x=6
n=len(arr)
if sum_x(arr,n,x):
   print("True")
else:
    print("False")