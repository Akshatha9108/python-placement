def findpair(a,n,x):
    a.sort()
    l=0
    r=n-1
    while(l<r):
        if (a[l]+a[r]==x):
            return True
        elif a[l]+a[r]>x:
             r=r-1
        else:
             l=l+1

    return False
a=[1,-2,1,0,5]
x=0
n=len(a)
if findpair(a,n,x):
    print("True") 
else:
    print("False")
        