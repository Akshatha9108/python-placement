def convert_to_integer(string):
    try:
        number=int(string)
        print("Integer value:",number)
    except ValueError:
        print("error:Invalid integer format!")

def main():
    str=input("enter a string to convert to integer:")
    convert_to_integer(str)
    