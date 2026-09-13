##Importing modules in Python:Modules and Packages
#In python, modules and packages help organize and reuse code. Here's a comprehensive guide on how to import them 

import math
print(math.sqrt(16))

#only importing a specific package
from math import sqrt,pi
print(math.sqrt(25))
print(pi)

#Importing as an alias
import numpy as np
print(np.array([1,2,3,4]))

#importing every module
from math import * 
print(sqrt(16))
