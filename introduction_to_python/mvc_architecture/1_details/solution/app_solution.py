from view_solution import capture_name,capture_age,display
from model_solution import details

name = capture_name()
age = capture_age()
data = details(name,age)
info = data.store(name,age)
display(info)
