try:
    n1=int(input("enter the first number:"))
    n2=int(input("enter second number:"))
    res=n1/n2
    print("Result:",res)
except ValueError:
   print("Invalid input.Please enter numeric values.")

except ZeroDivisionError:
   print("Error:cannot divide by zero")

else:  
  print("No exception occurred.")

finally:
  print("end of the program.")