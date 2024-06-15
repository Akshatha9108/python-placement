# An Equillibrium index is an index such that  sum of elements at lower indicies is equal to sum of elements at higher indices
def equilibrium_index(arr):
    n=len(arr)
    for i in range(n):
        lsum=sum(arr[:i])
        rsum=sum(arr[i+1:])
        if lsum==rsum:
            return i
    return -1
arr=[-7,1,5,2,-4,3,0]
print(equilibrium_index(arr))
