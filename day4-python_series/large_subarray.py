def largest_subarray_sum(ls):
    curr_sum=max_sum=ls[0]
    for i in ls[1:]:
        curr_sum=max(i,curr_sum+i)
        max_sum=max(curr_sum,max_sum)
    return max_sum
l=[-2,1,-3,4,-1,2,1,-5,4]
print(largest_subarray_sum(l))
