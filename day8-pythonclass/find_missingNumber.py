#Given an array of size n-1, such that it only contains distinct integers in the range of 1 to n. Find the missing element
# i/p : n=10, arr = [6,1,2,8,3,4,7,10,5]
def miss(n,arr):
  tot_sum = n*(n+1)//2
  arr_sum = sum(arr)
  return tot_sum - arr_sum
n = int(input("Enter no. of elements : "))
arr = list(map(int,input("Enter elements : ").split()))
print(miss(n,arr))