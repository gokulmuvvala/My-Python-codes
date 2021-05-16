# Function to demonstrate printing pattern
def pypart(n):
    # outer for loop to handle number of rows
    # n in this case
    for i in range(n):

        # inner for loop to handle number of columns
        for j in range(n):
            # printing #
            print("# ", end="")

        # ending line after each row
        print("\r") # "\r" is a carriage return

# Driver Code
n = 5
pypart(n)
