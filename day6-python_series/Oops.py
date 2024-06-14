#parent class
class Person(object):
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)
    def details(self):
        print(f"My name is {self.name}")
        print(f"Idnumber:{self.idnumber}")
#child class
class Employee(Person):
    def __init__(self, name, idnumber,salary,post):
        Person.__init__(self, name, idnumber)
        self.salary=salary
        self.post=post

    def details(self):
        print(f"My name is {self.name}")
        print(f"IDnumber is {self.idnumber}")
        print(f"Post: {self.post}")
#creation of an object variable or an instance
a=Employee('rahu',886012,20000,"Intern")
a.display()
a.details()