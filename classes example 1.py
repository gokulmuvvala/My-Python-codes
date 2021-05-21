# creating class

class mobile:
# declaring  function (inside the class functions are called as methods)
   def spec(self): # self is a pointer which refer to the current object 
        print("Poco X3 ")
        print("6gb ram")
        print("128gb storage")
        print("Version Android 10")

# Creating object 
spec1 = mobile() # object 1
spec2 = mobile() # object 2

# calling the methods
spec1.spec()
spec2.spec()
