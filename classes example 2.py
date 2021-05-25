# creating a class
class pc:
    
    # defining varibles with the help of __int__ method
    # self is a pointer which refer to the current object 
    def __init__(self,cpu,ram,brand): # __init__ is a special method it used intialize the variables 
        self.cpu = cpu  # cpu instance  variable is created
        self.ram = ram  # ram instance  variable is created
        self.brand = brand # brand variable is created
# defining the method
    def lapi(self):
        # here we need use self. because cpu,ram,brand are not global variables  
        print("CPU   : ",self.cpu) # this all are a
        print("RAM   : ",self.ram)
        print("BRAND : ",self.brand)

# creating the objects
pc1 = pc('i5',16,"DELL")  # object 1
pc2 = pc('i7',8,"HP") # object 2

# calling the methods 
pc1.lapi()
pc2.lapi()