##Python memory management 
'''Memory management in python involves a combination of automatic garbage collection, 
   refrence countiing, and various internal optimizations to efficiently manage memory allocation and deallocation
'''

'''1. Key concepts in pyhton memory management 
   2. Memory allocation and deallocation
   3. Reference Counting
   4. Garbage Collection
   5. The gc module
   6. Memory Management Best Practices
'''

##Reference counting 
'''Reference counting is a primary method in python uses to manage memory.
   Each Object in python maintains a count of references pointing to it. 
   When the reference count drops to zero, the memory is occupied the by the object.  
   '''

import sys #System configuration
a = [] ## Output 2 (One reference is coming from 'a' and one from getrefcount())
print(sys.getrefcount(a))

b=a
print(sys.getrefcount(a))

del b
print(sys.getrefcount(a))


##Garbage collection
'''
Python includes a cyclic garbage collector to handle refernce cycles. Reference cycles occur when objects 
reference each other, preventing their reference counts from reaching zero.
'''
import gc
##Enable the garbage collection
gc.enable()
gc.disable()
print(gc.collect()) #number of unreachable objects 

##Get garbage collection stats
print(gc.get_stats())

##Get unreachable objects 
print(gc.garbage)