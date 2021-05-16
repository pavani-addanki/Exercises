from view_solution import ask_filename, ask_content, display
from model_solution import Create_File

file_name = ask_filename()
content = ask_content()
data = Create_File(file_name, content)
data.create()
data.write()
result = data.read()
display(result)