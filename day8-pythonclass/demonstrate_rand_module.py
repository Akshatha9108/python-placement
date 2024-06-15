import random #generate floating point
def demonstrate_random_module():
    print("Random module demonstration:")

    #random.random()-return a random float in the range[0.0,1.0]
    print("\nrandom.random():")
    print(random.random())

    #random.uniform(a,b)-returns a random float in the range[a,b]
    print("\nrandom.uniform(1,10):")
    print(random.uniform(1,10))

    #random.randint(a,b)-return a random integer in the range [a,b]
    print("\nrandom.uniform(1,10):")
    print(random.randint(1,10))

    #random.randrange(start,stop,step)-returns a randomly selected element 
    print("\nrandom.randoarrange(1,10,2):")
    print(random.randrange(1,10,2))

    #random.choice
    my_list=[1,2,3,4,5]
    print("\nrandom.choices([1,2,3,4,5]):")
    print(random.choice(my_list))

    #random.choices(seq,weights=None,k=1)-returns a list with k randomly
    my_list=[1,2,3,4,5]
    print("\nrandom.choices([1,2,3,4,5],k=3):")
    print(random.choices(my_list,k=3))

    #random.sample(seq,k)-returns a list of k unique randomly selected element
    print("\nrandom.sample([1,2,3,4,5],k=3):")
    print(random.sample(my_list,k=3))

    #random.shuffle(X)- shuffles the sequence x in place
    print("\nrandom.shuffle([1,2,3,4,5]:)")
    random.shuffle(my_list)
    print(my_list)

    #random.seed(A=None) - initializes the random number generator
    print("\nrandom.seed(10) and random.random():")
    random.seed(10)
    print(random.random())

    #random.getrandbits(k)
    print("\nrandom.getrandbits(5):")
    print(random.getrandbits(5))

    #random.gauss(mu,sigma)
    print("\nrandom.gauss(0,1):")
    print(random.gauss(0,1))

if __name__=="__main__":
    demonstrate_random_module()