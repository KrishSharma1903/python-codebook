lst = list(range (1, 21))
print(lst)

# print(f"First element: {lst[0]}")
# print(f"Middle element: {lst[len(lst) // 2]}")
# print(f"Last element: {lst[-1]}")


# print(f"First five elements: {lst[:5]}")
# print(f"Last five elements: {lst[-5:]}")
# print(f"Elements from index 5 to 15: {lst[5:16]}")

# squares = [x**2 for x in range(1, 11)]
# print(squares)


even = [x for x in lst if x%2 == 0]
print(even)
