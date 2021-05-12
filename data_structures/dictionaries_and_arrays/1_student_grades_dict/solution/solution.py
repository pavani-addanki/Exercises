letter_grades_1 = dict()
for i in range(0, 101):
    if i>=90:
        letter_grades_1[i] = "A"
    elif i>=75:
        letter_grades_1[i] = "B"
    elif i>=60:
        letter_grades_1[i] = "C"
    elif i>=45:
        letter_grades_1[i] = "D"
    elif i>=30:
        letter_grades_1[i] = "E"
    elif i>=1:
        letter_grades_1[i] = "F"
'''
letter_grades_1 = {1: 'F', 2: 'F', 3: 'F', 4: 'F', 5: 'F', 6: 'F', 7: 'F', 8: 'F', 9: 'F', 10: 'F', 11: 'F', 12: 'F', 13: 'F', 14: 'F', 15: 'F', 16: 'F', 17: 'F', 18: 'F', 19: 'F', 
20: 'F', 21: 'F', 22: 'F', 23: 'F', 24: 'F', 25: 'F', 26: 'F', 27: 'F', 28: 'F', 29: 'F', 30: 'E', 31: 'E', 32: 'E', 33: 'E', 34: 'E', 35: 'E', 36: 'E', 37: 'E', 38: 'E', 39: 'E',
 40: 'E', 41: 'E', 42: 'E', 43: 'E', 44: 'E', 45: 'D', 46: 'D', 47: 'D', 48: 'D', 49: 'D', 50: 'D', 51: 'D', 52: 'D', 53: 'D', 54: 'D', 55: 'D', 56: 'D', 57: 'D', 58: 'D', 59: 'D', 60: 'C', 61: 'C', 62: 'C', 63: 'C', 64: 'C', 65: 'C', 66: 'C', 67: 'C', 68: 'C', 69: 'C', 70: 'C', 71: 'C', 72: 'C', 73: 'C', 74: 'C', 75: 'B', 76: 'B', 77: 'B', 78: 'B', 79: 'B', 80: 'B', 81: 'B', 82: 'B', 83: 'B', 84: 'B', 85: 'B', 86: 'B', 87: 'B', 88: 'B', 89: 'B', 90: 'A', 91: 'A', 92: 
'A', 93: 'A', 94: 'A', 95: 'A', 96: 'A', 97: 'A', 98: 'A', 99: 'A', 100: 'A'} 
'''

import math

def student_grades(sgrades, letter_grades):
    temp_dict = {}
    avg_dict = {}
    stu_grad = {}

    for i,j in sgrades.items():
        # print(int(sum(j)/len(j)))
        avg=int(sum(j)/len(j))
        avg_dict[i] = avg
    for name in avg_dict:
        stu_grad[name] = (letter_grades_1[avg_dict[name]], avg_dict[name] )
    print(stu_grad)
    return stu_grad