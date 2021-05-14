from view_solution import display
from model_solution import Student
result=Student(1,'Jack')
result2=Student(2,'Paul')
result.create()
data=result.query()
# data=result2.query()
display(data)