def find_richest_customer(accounts):
    max_wealth=0
    for cus in accounts:
        wealth=sum(cus)
        if wealth>max_wealth:
            max_wealth=wealth
    return max_wealth
if __name__ == "__main__":
    m=int(input("enter no of customers:"))
    n=int(input("Enter number of banks:"))
    acc=[]
    for i in range(m):
        print(f"Enter wealth for customer{i+1}in {n}banks:")
        customer_wealth=list(map(int,input().split()))
        acc.append(customer_wealth)
    print(find_richest_customer(acc))