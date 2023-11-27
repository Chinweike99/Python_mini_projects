#!/usr/bin/python3

student_mark = {
        "Jacob": 87,
        "Favour": 15,
        "Innocent": 95,
        "Peter": 98,
        "Mark": 76,
        "Dominion": 10,
        "Felix": 57,
        "Clement": 44,
        "Frank": 28,
        "Anthony": 60,
        "Stanley": 50,
        "Sylvester": 39,
        "Caleb": 19,
        "Noah": 21
        }

student_grade = {}
for key in student_mark:
    mark = student_mark[key]
    if mark >= 90:
        student_grade[key] = 'A+'
    if mark >= 80:
        student_grade[key] = 'A'
    if mark >= 70:
        student_grade[key] = 'B+'
    if mark >= 60:
        student_grade[key] = 'B'
    if mark >= 50:
        student_grade[key] = 'C'
    if mark >= 40:
        student_grade[key] = 'D'
    if mark >= 30:
        student_grade[key] = 'E'
    if mark >= 20:
        student_grade[key] = 'F'
    else:
        student_grade[key] = 'NOT A STUDENT'

print(f"{key, student_grade}'s grade: {student_grade}\n")

#print(student_mark)
#print(f"{student_grade}")
