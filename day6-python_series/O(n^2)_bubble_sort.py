def bubble_sort(a):
    n=len(a)
    for i in range(n):
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
arr=[60,40,30,90,20]
bubble_sort(arr)
print("Sorted array",arr)