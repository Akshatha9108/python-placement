def peak(list):
    if not list:
        return None
    l,r=0,len(list)-1
    while(l<r):
        mid=l+(r-l)//2
        if list[mid]<list[mid+1]:
            l=mid+1
        else:
            r=mid
    return list[l]

ls=[1,2,1,3,5,6,4]
print(peak(ls))