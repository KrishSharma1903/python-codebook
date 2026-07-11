student_score = {
    "Student 1" : 94,
    "Student 2" : 50,
    "Student 3" : 25,
    "Student 4" : 88,
    "Student 5" : 70,
}

student_grades = {}

for key in student_score:
    score = student_score[key]

    if score >= 91:
        student_grades[key] = "Outstanding"
    if score >= 81:
        student_grades[key] = "Good"
    if score >= 71:
        student_grades[key] = "Could have been better"
    else:
        student_grades[key] = "Fail"


for i in student_grades:
    print(i)
    print(student_grades[i])
    
    
    
    