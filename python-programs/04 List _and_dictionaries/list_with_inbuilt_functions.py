import random

random_numbers = [random.randint(1, 20) for _ in range(15)]
print(f"Original list: {random_numbers}")

sorted_numbers = sorted(random_numbers)
print(f"Sorted in ascending order: {sorted_numbers}")

sorted_numbers_desc = sorted(random_numbers, reverse=True)
print(f"Sorted in descending order: {sorted_numbers_desc}")

unique_numbers = list(set(random_numbers))
print(f"List with duplicates removed: {unique_numbers}")