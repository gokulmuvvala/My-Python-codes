# Duck typing example in oops
# defining the ide (Not user defined )
class Pycharm:
     # creating a method to execute the ide  
    def execute(self):
        print("Compile")
        print("run")

# defining user defining ide 
class  becharm: # this is user created ide name 
    # creating a method to execute the ide  
    def execute(self):
        print("Compile")
        print("Debug")
        print("Executes") 
# class definition
class laptop:
        # creating the method
    def code(self,ide): 
        ide.execute()  # here in this method we want to execute ide(User defined ide) 


# creating the object 
ide = becharm() # defining becharm as ide 
lapi1 = laptop()  

# calling method    

lapi1.code(ide)


