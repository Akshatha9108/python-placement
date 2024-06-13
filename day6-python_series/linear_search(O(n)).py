def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i #target found retrun its index
    return -1 #target not found 

arr=[9,6,4,3,32,1,8]
target=32
result=linear_search(arr,target)
if result!=-1:
    print(f'Element found at index: {result}')
else:
    print("Element not found in the array")