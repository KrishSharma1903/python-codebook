##Memory Management best practices
'''
1. Use Local variables: Local variables have a shorter lifespan and are freed sooner than global variable 
2. Avoid Circular references: Circular references can lead to memory leaks if not properly managed 
3. Use Generators: Generators produce items one at a time and only keep one item in memory at a time,
                    making the memory efficient 
4. Explicity delete objects: Use the del statement to delete variables and objects explicitly
5. Profile memory usage: Use memory profiling tools like tracemalloc and memory_profilier to identify memory leaks and
                         optimize memory usage.
'''

import gc 

class MyObject:
    def __init__(self,name):
        self.name = name 
        print(f"Object {self.name} created")


    def __del__(self):
        print(f"Object {self.name} deleted")

##Create a circular reference 
obj1 = MyObject("Obj1")
obj2 = MyObject("Obj2")

obj1.ref=obj2
obj2.ref=obj1

del obj1
del obj2

##Manually trigger the garbage collection
gc.collect()