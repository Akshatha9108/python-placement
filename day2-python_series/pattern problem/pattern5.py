n=int(input())
for i in range(1,n):
    for j in range(1,n):
        if j<=i:
            print(i,end=' ')
    print()