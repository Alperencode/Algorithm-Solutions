# Grading Students
# https://www.hackerrank.com/challenges/grading/problem

def gradingStudents(grades):
    for index, grade in enumerate(grades):
        if grade % 5 >= 3 and grade >= 38:
            grades[index] += 5-grade % 5
    return grades

# Testcases
# 73 67 38 33 - 75 67 40 33

# Status - Passed
