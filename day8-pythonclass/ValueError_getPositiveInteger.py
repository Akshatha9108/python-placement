def get_positive_integer():
    while True:
        try:
            number=int(input("Enter a positive integer:"))
            if number<=0:
                raise ValueError("Not a positive integer!")
            return number
        except ValueError as e:
            print("Error:",e)

positive_integer=get_positive_integer()
print("yoy entered:",positive_integer)