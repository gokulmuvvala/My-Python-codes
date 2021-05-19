# finding factorial of a number using functions
n = int(input("Enter the number = "))
def fact(n):

    f = 1  # f is a temp variable 

    for i in range(1,n+1):  # here n+1 for ending the multiplication
        f = f*i  
    return f

result = fact(n)

print(result)