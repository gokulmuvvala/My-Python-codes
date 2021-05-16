from numpy import *
arr1 = array([1,2,3,4,5,6,7,8,9])
arr2  = array([2,6,4,9,7,8,9,6,4])
arr1 = arr1 + 5 # adding 5 to each element in array(arr1)
print(arr1)
arr1 = arr1 - 5 # subtracting 5 to each element in array(arr1)
print(arr1)
print("")
# Adding 2 array arr1 + arr2 
arr3 = arr1 + arr2
print(arr3)
print("")
print(sin(arr3)) # finding the sin values of arr3
print("")
print(log(arr3)) # finding the log values of arr3
print("")
print(sqrt(arr3)) # finding the square root of values of arr3
print("")
print(sum(arr3)) # finding the sum values of arr3
print("")
print(max(arr3)) # finding the max value of arr3
print("")
print(min(arr3)) # finding the min value of arr3
print("")
print(concatenate([arr1,arr2])) # mergeing of 2 arrays
 
