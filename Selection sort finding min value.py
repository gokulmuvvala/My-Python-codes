# selection sort finding min value
#defining th function
def sort(list):
    # This outer loop is for check the number of elements we have  
    for i in range(5):
        minpos = i # minimum position = i
        for j in range(i,6): # i,length of an list
            if list[j] < list[minpos]:
               minpos = j

        # swapping
        temp = list[i]
        list[i] = list[minpos]
        list[minpos] = temp


         

list = [ 52, 88, 55, 77, 2, 71] # unsorted list
# calling the function 
sort(list)

print (list) # sorted list