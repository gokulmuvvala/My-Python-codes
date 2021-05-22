# Example with both the class variables and instance variables 
class Car:
    # declaring the class variables 
    wheels = 4 # wheels a class variable is created 
    fuel_type = "petrol"
    # declaring the instance variables 
    def __init__(self):
        self.company = "Ford"
        self.color  = "White"
        self.millage =  12
            

# creating a objects
car1 = Car()    # Car 1 object is created 
car2 = Car()    # Car 2 object is created 
car3 = Car()    # Car 3 object is created 

# # changing the variable values 
car2.company = "Hyundai"
car2.wheels =  5    # changing the class variable with the help of object name
Car.fuel_type = "Disel" # changing the class variable with the help of Class name
# # printing the objects
# ## calling the class variables and instance variables  with the help of object name 
print (car1.company, car1.color, car1.millage, car1.wheels, car1.fuel_type)  
print (car2.company, car2.color, car2.millage, car2.wheels, car2.fuel_type) 
print (car3.company, car3.color, car3.millage, car3.wheels, car3.fuel_type)
