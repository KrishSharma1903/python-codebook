##Mathematical Operations
set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}

#union 
union_set = set1.union(set2)
print(union_set)

#intersection
intersection_set = set1.intersection(set2)
print(intersection_set)

#intersection_update
set1.intersection_update(set2)
print(set1) #updates the intersection value into set1

set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}

#Difference
print(set1.difference(set2)) 

#Symmetric Difference
print(set1.symmetric_difference(set2)) #unique elements from both the sets are combined  

#Set method 
set1 = {1,2,3,4,5}
set2 = {3,4,5}
#is subset
print(set1.issubset(set2))
print(set1.issuperset(set2))

#remove the duplicates from a list
lst=[1,2,2,2,3,3,3,4,5,]
print(set(lst))
