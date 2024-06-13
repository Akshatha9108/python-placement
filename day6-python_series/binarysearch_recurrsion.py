def bs_r(a,t,l,r):
    if (l>r):
        return -1 #base case:target not found
    mid=l+(r-l)//2
    if a[mid]==t:
        return mid #target found return theindex
    elif a[mid]<t:
        return(bs_r(a,t,mid+1,r))
    else:
        return (bs_r(a,t,l,mid-1))
arr=[1,2,3,4,5,6,7,8,9]
n=len(arr)
l=0
r=n-1
target=5
result=bs_r(arr,target,l,n-1)
if result!=-1:
    print(f'Element found at index:{result}')
else:
    print("Element not found in the array")    
    
    