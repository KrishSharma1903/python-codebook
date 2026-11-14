def check_unique(lst):
    seen=set()
    for num in lst:
        if num in seen:
            return False
        else:
            seen.add(num)
    return True

print(check_unique([1,2,2,3,4,5,6]))
print(check_unique([1,2,3,4,5,6]))