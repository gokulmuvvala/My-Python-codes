# Decorators example 
# existing function 
def div(a,b):
    print (a/b)
 
# newly created function
def new(func):
    # extra features function( function in function )
    def inner (a,b):
        if a < b:
           a,b = b,a
        return func(a,b)
 
    return inner 
 
# updating the existing function with the newly created function
div = new(div)
 
# function calling with added features 
div(2,4)
     
 
