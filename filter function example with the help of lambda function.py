# example with the help of lambda function
# finding even numbers from given list
# doubling the numbers in the given list
# Adding the numbers in a given list  
# Taking the input from the user by the help of 
from  functools import * 
nums = [22,94,42,37,6,12, 35]
evens = list(filter(lambda n : n%2 == 0, nums))  # instead of function declaration and function calling we are using this line 
print(evens)

doubles =  list(map(lambda  n : n*2 , evens)) # Here we are doubling the previuosly finded even numbers 

print(doubles)

sum = reduce(lambda a,b : a+b,doubles) # reduce(logic function,sequence)

print (sum)
