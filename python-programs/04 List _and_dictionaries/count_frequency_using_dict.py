numbers =[1,1,1,1,2,2,2,3,3,3,4,4,4]
frequency={}

for i in numbers:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
print(frequency)