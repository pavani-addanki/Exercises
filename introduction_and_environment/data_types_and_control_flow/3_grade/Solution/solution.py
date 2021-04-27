# Code your solution here
from provided_code import grades

letter_grades = []

for marks in grades:
    if(marks >= 90 and marks <= 100):
        letter_grades.append('A')
    elif(marks >= 70 and marks <= 89):
        letter_grades.append('B')
    elif(marks >= 50 and marks <= 69):
        letter_grades.append('C')
    elif(marks >= 35 and marks <= 49):
        letter_grades.append('D')
    elif(marks < 35):
        letter_grades.append('F')



