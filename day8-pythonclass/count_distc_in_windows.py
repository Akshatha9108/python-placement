#Given array of integers and number K find the count of distinct element in every window of size in the array

def count_dist_of_windowa(arr,n,k):
    res=[]
    for i in range(n-k+1):
        window=arr[i:i+k]
        distinct_count=len(set(window))
        res.append(distinct_count)
    return res
n=int(input("enter the number of elements:"))
arr=[]
for j in range(n):
    arr.append(int(input()))
k=int(input("Enter the size of the window:"))
res=count_dist_of_windowa(arr,n,k)
for count in res:
    print(count,end='\t')
               