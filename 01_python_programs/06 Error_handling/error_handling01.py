# #eg 1
# try: 
#     a=b
# except NameError as ex:
         # print(ex)


#  eg 2 
# try:
#     result =  12/0
# except ZeroDivisionError as ex:
#     print(ex)


#eg 3

try:
    result = 1/0
except ZeroDivisionError as ex:
    print(ex)
except Exception as ex1:
    print(ex1)