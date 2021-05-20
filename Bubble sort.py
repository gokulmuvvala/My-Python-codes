# bubble sort
#defining th function
def sort(list):
    # This outer loop is for check the number of elements we have  
    for i in range(len(list)-1,0,-1):  # here we are going from index 5 to index 0
        # This inner loop is for swapping the elements  
        for j in range(i):   #here we are going from j to range of i
            #swapping elements with the help of temp element 
            if list[j]> list[j+1]:  
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

list = [ 52, 88, 55, 77, 2, 71] # unsorted list
# calling the function 
sort(list)

print (list)