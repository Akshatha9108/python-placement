#O(2**n)
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
n=6
res=fib(n)
print(f"The {n}th fibonacci number is:",res)