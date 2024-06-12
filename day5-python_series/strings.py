#entr string
s=input("enter a string:")
#string length
print("length of the string:",len(s))
print("----------------------------")
#convert to uppercase
print("uppercase:",s.upper())
print(s.isupper())

#convert to lowercase
print("Lowercase:",s.lower())
print(s.islower())
print("----------------------------")

#capitalize the string '
print ("Capitalized:",s.capitalize())
print("Capitalized every single word:",s.title())
print("----------------------------")

#COUNT OCCURRENCES OF A SUBSTRING
substring=input("enter  a substring to count its occurences:")
print("occurences of:",substring,"in the string:",s.count(substring))
print("----------------------------")

#check if the strng starts with a specific substring 
prefix=input("enter a prefix to check if the string starts with it:")
print("Starts with:",prefix,":",s.startswith(prefix))
print("----------------------------")

#check if the string end with a specific substring 
suffix=input("Enter a suffix to check if the string ends with it:")
print("ends with",suffix,":",s.endswith(suffix))
print("----------------------------")

#Replace a substring with  another substring
old=input("enter a substring to replace:")
new=input("emter a replacment substring:")
print("after Replacement :",s.replace(old,new))
print("----------------------------")

#split the string into a list of substrings
delimiter=input("enter a delimiter to split the string:")
print("Split string :",s.split(delimiter))
print("----------------------------")

#Join a list of substring into a single strng
substrings=input("enter a substring to join (separated by space):").split()
join_delimiter=input("enter a delimiter to join the substirng:")
print("joined String:",join_delimiter.join(substrings))
print("----------------------------")

#the strip() method removes any whitespace from the beginning or the end:
print(s.strip())
#print(s.lstrip())
#print(s.rstrip())
#print(s.rjust())
print(s.rfind("l"))
print(s.rindex("l"))