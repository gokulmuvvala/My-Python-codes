from numpy import *
arr = array([4,56,2,9,8,6,12,46,19]) 

# initializing max with 1st element in the array 
max = arr[0]

for i in range(0, len(arr)): # here range is from 0 to end element of arr
    # comparing the elements with the max
    if (arr[i]>max):
        max = arr[i]

    print ("The largest element in the given array is" +str(max))
    
    
