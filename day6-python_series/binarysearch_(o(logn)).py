#O(logn)
def binary_search_iterative(arr,target):
    left,right=0,len(arr)-1

    while left<=right:
        mid=left+(right-left)//2
        if arr[mid]== target:
            return target
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
arr=[1,2,3,4,5,6,7,8,9]
target=5
result=binary_search_iterative(arr,target)
if result!=-1:
    print(f'Element found at index{result}')
else:
    print("Element not found in the array")