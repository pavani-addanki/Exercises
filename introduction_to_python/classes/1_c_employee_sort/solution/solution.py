class Employee:
    employee_lst = []      

    def __init__(self,name,employee_id,salary,years_at_company):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.years_at_company = years_at_company

def sort_employees(employee_lst):
    sort_emp_names = []
    for emp in employee_lst:
        sort_emp_names.append(emp.name)
    sort_emp_names.sort()
    return sort_emp_names   
        

