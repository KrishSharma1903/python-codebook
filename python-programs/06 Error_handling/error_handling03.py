try:
    num = int(input("Enter a number: "))
    result = 10 / num

except ValueError:
    print("Enter a valid number")

except ZeroDivisionError:
    print("Enter a number greater than zero")

except Exception as ex:
    print(ex)

else:
    print(f"Your reuslt is {result}")

finally:
    print("Program has executed")