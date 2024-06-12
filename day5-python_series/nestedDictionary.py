myfamily={
    "child1":{
        "name":"Emi",
        "year":2004
    },
    "child2":
    {
        "name":"Tobias",
        "year":3004
    },
    "child3":
    {
        "name":"linus",
        "year":2011
    }
}
print(myfamily)
print(myfamily["child2"]["name"])
for x, obj in myfamily.items():
    print(x)
    for y in obj:
        print(y+':',obj[y])