##Generators
'''Generators are a simpler way to create iterators. They use the yield keyword to produce a series of values lazily, 
which means they generate values on the fly and do not store them in memory.'''

def square(n):
    for i in range(3):
        yield i**2 #saves and returns the value 
print(square(3))

for i in square(3):#printing 
    print(i)

a=square(3)#another way to print 
print(next(a))

#Example 
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(gen)
print(next(gen))

for val in gen:
    print(val)