# This is python program to find K'th smallest
def Kthsmallest(arr,b,k): # function to return K'th smallest

    arr.sort()

    return arr[k-1]

if __name__== '__main__':
    arr = [11,3,6,7,22] # here we are entering the variables into array
    n= len(arr) # n describes the length of array
    k=2
    print("K'th smallest element =", Kthsmallest(arr,n,k))