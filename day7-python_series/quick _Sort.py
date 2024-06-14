def quick_sort(a):
    if len(a)<=1:
        return a
    pivot=a[len(a)//2]
    left=[x for x in a if x<pivot]
    mid=[x for x in a if x==pivot]
    right=[x for x in a if x>pivot]
    return quick_sort(left)+mid+quick_sort(right)

arr=[12,11,32,5,6,7]
print("Given array is :",arr)
sorted=quick_sort(arr)
print("Sorted array is:",sorted)