#write s program to partition a list around a givrn value
def partition_list(list,pivot):
    less_than=[x for x in list if x< pivot]
    equal_to=[x for x in list if x== pivot]
    greater_than=[x for x in list if x > pivot]

    return less_than+equal_to+greater_than

lst=[3,1,4,1,5,9,2,6,5]
pivot_value=4
print(partition_list(lst,pivot_value))