'''Python standard library is a vast collection of modules and packages that come bundled with python, 
providing a wide range of functionalities out of the box'''

#array
import array
arr = array.array("i",[1,2,3,4])
print(arr)

#math
import math
print(math.sqrt(16))
print(math.pi)

#random
import random
print(random.randint(1,10))
print(random.choice(['apple','mango','cherry']))

##File and Directory Access (OS)
import os 
print(os.getcwd())

# os.mkdir('test.dir')

#High level operations on the files and collection of files 
import shutil
# shutil.copyfile('source.txt','destination.txt')

# Data Serialization
import json
data= {"name":"Krish","Age":21}
json_str=json.dumps(data)
print(type(json_str))
print(json_str)

parsed_data=json.loads(json_str)
print(parsed_data)
print(type(parsed_data))

##csv
import csv
with open('example.csv',mode='w',newline="") as file:
    writer=csv.writer(file)
    writer.writerow(['name','age'])
    writer.writerow(['Krish','21'])

with open('example.csv',mode='r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

#date-time
from datetime import datetime,timedelta
now=datetime.now()
print(now)

yesterday = now-timedelta(days=1)
print(yesterday)

#time 
import time 
print(time.time())
time.sleep(2)
print(time.time())

#Regular expression 
import re
pattern=r'\d+'
text = 'There are 123 apples'
match=re.search(pattern,text)
print(match.group())