#!/usr/bin/python3
"""
A Modeule for grades assignment to students scores using conditions
"""

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

def grade(score):
    """Function to assign grades to Scores"""
    for key in student_mark:
        if score > 90:
            return 'A+'
        elif score > 80:
            return 'A'
        elif score > 70:
            return 'B+'
        elif score > 60:
            return 'B'
        elif score > 50:
            return 'C'
        elif score > 40:
            return 'D'
        else:
            return 'FAILD'

for key, value in student_mark.items():
    result = grade(value)
    print(f"{key}'s grade: {result}")
