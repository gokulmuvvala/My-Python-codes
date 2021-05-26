# Generator example
# defining the generator
def topten():

    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


# creating the object

values = topten() # object 1 is craeted 

# printing the topten

print(values.__next__())

print(values.__next__())
print(values.__next__())

print(values.__next__())
print(values.__next__())

# we can also for loop to print the the top ten 
