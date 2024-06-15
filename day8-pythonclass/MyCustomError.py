class MyCustomError(Exception):
    def __init__(self, message):
        self.message=message
try:
    raise MyCustomError("this is a custom error message")
except MyCustomError as e:
    print("Custom error caught:",e.message)
#except Exception as e:
#    print("An Error occurred:",e)