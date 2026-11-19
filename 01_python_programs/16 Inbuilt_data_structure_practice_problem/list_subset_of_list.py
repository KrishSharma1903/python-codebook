def is_subset(lst1, lst2):
    for x in lst1:
        found = False

        for y in lst2:
            if x == y:
                found = True
                break

        if not found:
            return False

    return True

print(is_subset([1, 2, 3], [1, 2, 3, 4, 5]))