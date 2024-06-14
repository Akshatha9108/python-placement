def mergesort(a):
    if len(a)>1:
        #create sub_arr2<--a[start....mid]and sub_arr2
        mid=len(a)//2
        s1=a[:mid]
        s2=a[mid:]

        #sort the two halves
        mergesort(s1)
        mergesort(s2)

        #initializinge i ,j,k
        i=j=k=0

#until we reach end of either start or end,pick larger
#elements start  and end and place them in the correct position
        while i <len(s1)and j<len(s2):
            if s1[i]<s2[j]:
                a[k]=s1[i]
                i+=1
            else:
                a[k]=s2[j]
                j+=1
            k+=1
        while i<len(s1):
            a[k]=s1[i]
            i+=1
            k+=1
        while j<len(s2):
            a[k]=s2[j]
            j+=1
            k+=1

arr=[10,9,2,4,6,13]
mergesort(arr)
print(arr)