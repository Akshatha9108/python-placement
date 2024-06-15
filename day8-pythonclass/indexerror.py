def access_list_element(lst,index):
    try:
        value=lst[index]
        print("Value at index",index,"is:",value)

    except IndexError:
        print("Error :Index out of range!")

mylist=[1,2,3,4,5]
index=int(input("Enter an index to access:"))
access_list_element(mylist,index)