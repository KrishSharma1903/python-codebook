def count_even_odd(lst):
    count_odd = 0
    count_even = 0  

    for i in lst:
        if i%2==0:
            count_even +=1
        else:
            count_odd +=1 

    return (count_even, count_odd)

print(count_even_odd([1, 2, 3, 4, 5]))