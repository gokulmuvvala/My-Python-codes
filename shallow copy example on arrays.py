# shallo copy
from numpy import *
arr1 = array( [36,69,3,9,8,7,65,82,16])
arr2 = arr1.view() # view is a function which will help u create an array 
print(arr1)
print(arr2)

print(id(arr1)) # id used find address of array
print(id(arr2))  