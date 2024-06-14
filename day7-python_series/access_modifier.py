class Super:
    #public data member 
    var1=None
    #protected data member
    _var2=None
    #private data member
    __var3=None

    #constructor
    def __init__(self,var1,var2,var3):
        self.var1=var1
        self._var2=var2
        self.__var3=var3

    #public member function
    def displayPublicMembers(self):

        #accessing public data members
        print("Public data member:",self.var1)

    #protected member function
    def _displayProtectedMembers(self): # _ for protected memeber

        #accessing protected data members
        print("Protected Data member:",self._var2)

    #privated member function
    def __displayPrivateMembers(self): # _ _ for private mpre secure and protected
        #accessing private data members
        print("Private data member:",self.__var3)

    #private member function
    def accessPrivateMembers(self):
        #accessing private member function
       self.__displayPrivateMembers()

#derived class
class Sub(Super):
    #constructor
    def __init__(self, var1, var2, var3):
        super().__init__(var1, var2, var3)

    #public member function
    def accessProtectedMembers(self):
        #accessing protected member function of super clss
        self._displayProtectedMembers()

#creating objects
obj=Sub("Hello","all","people!")

#calling public member functions of the class
obj.displayPublicMembers()
obj.accessProtectedMembers()
obj.accessPrivateMembers()

#object can acess protected member
print("object is accessing protected member:",obj._var2)

#object can not access private member,so it will generate attribute
#print(obj.__var3)
