# exception handling in python example
a = 5
b = 0
try: # try block used when a critical statement is there
    print(a/b) # critical statement 
except Exception as e: # this will except the error  (we can use any variable not only e)
    print ("Hey, you can't divide a number by the Zero !!!", e)  # user (or) developer defined  error message (here e will say what type of error )
print("try is special")