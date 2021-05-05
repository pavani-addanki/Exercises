class Student:
    def __init__(self, name : str, age: int, grades:[]):
        self.name = name
        self.age = age
        self.grades = grades

def highest_avg(stud_lst):
    stu_avg = {}
    final_stu = []
    student = ""
    for i in stud_lst:
        avg = sum(i.grades)/len(i.grades)
        stu_avg[i.name] = avg
    a = sorted(stu_avg.items(), key=lambda x: x[1])
    print(a)
    if len(stud_lst) > 1:
        if a[-1][1] == a[-2][1]:
            final_stu.append(a[-1][0])
            final_stu.append(a[-2][0])
            final_stu.sort()
            student = final_stu[0]
        else:
            student = a[-1][0]
    else:
        student = a[-1][0]

    return student