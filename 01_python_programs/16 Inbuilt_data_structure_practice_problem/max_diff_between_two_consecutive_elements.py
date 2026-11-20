def max_consecutive_difference(numbers):
    left = 0
    right = 1
    max_difference = 0
    list_length = len(numbers)

    while right < list_length:
        difference = abs(numbers[left] - numbers[right])

        if difference > max_difference:
            max_difference = difference

        left += 1
        right += 1

    return max_difference

print(max_consecutive_difference([1, 7, 3, 10, 5]))