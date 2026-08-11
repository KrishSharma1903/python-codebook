def check_unique(lst):
    seen = set()
    
    for i in lst:
        if i in seen:
            return False
        seen.add(i)
    return True


print(check_unique([1,1,1,1,2,3,4,5,6,7,7,8,8,9]))