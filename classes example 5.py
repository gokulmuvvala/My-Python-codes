# inner class example
# inner class is nothing but a class inside the class
# outer class
class student: 

# defining the instance variables with the help of __init__ method 
    def __init__(self,name,roll): # taking the input after the object is created
        self.name = name 
        self.roll = roll
        # inner class variables declaration
        self.lapi = self.laptop() # variable name can be anything
        # defining show method    
    def show(self):
        print(self.name,self.roll) 
# inner class ( class inside the student class)
    class laptop:
# defining the instance variables with the help of __init__ method 
        def __init__(self):
            self.brand = "DELL"
            self.ram = 16
            self.cpu = "i5"
# crerating the objects 
s1 = student('Ravi kiarn',24)
s2 = student("Gokul",30)

# calling the show function for printing the inner class
s1.show()
s2.show()
