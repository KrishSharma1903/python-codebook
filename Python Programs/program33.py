student_Score =[95, 90, 58, 34, 45, 45, 63, 63, 16, 75, 35]

total_sum = print(max(student_Score))


max_score = 0
for i in student_Score:
    if max_score < i:
        max_score = i

print(max_score)