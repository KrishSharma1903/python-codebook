## for loop 
# we use range function range(5) gives -> 0,1,2,3,4
for i in range(5):
    #print(i)
    continue

#Custom range 
for i in range(1,6):
    #print(i)
    continue

#Step inside range
for i in range(1,10,2):
    #print(i)
    continue

#To start from the end 
for i in range(10,1,-1):
    #print(i)
    continue

#for loops in string 
str = "krish Sharma "

for i in str:
    #print(i)
    continue


# while loop
#  The while loop executes as long as the condition is True

count = 0
while count < 5:
    break
    print(count)
    count += 1


###Loop control statement

##break statement
# The break statement exits the loop prematurely

for i in range(10):
    break
    if i==5:
        break
    else:
        print(i)

##Continue Statement 
#The continnue statement skips the current iteration and continues with the next.

for i in range(10):
    break
    if i%2==0:
        continue
    else:
        print(i)

##Pass statement 
# The pass statement is a null operation; it does nothing 

for i in range(5):
    break
    if i==3:
        pass
    print(i)



## Nested loops
# a loop within a loop

for i in range(3):
    for j in range(2):
        print(f"i:{i} and j:{j}")
        