from custom_package.maths import add

print(add(2,3))

#OR
from custom_package import maths
print(maths.add(2,3))

#importing a subpackage
from custom_package.sub_packages.mult import mult
print(mult(2,3))