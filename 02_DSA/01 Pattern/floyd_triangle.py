def generate_floyds_triangle(n):
    lst = []
    num = 1

    if 1 <= n <= 100:
        for i in range(1, n + 1):
            row = []

            for j in range(i):
                row.append(str(num))
                num += 1

            lst.append(" ".join(row))

        return lst

print(generate_floyds_triangle(5))