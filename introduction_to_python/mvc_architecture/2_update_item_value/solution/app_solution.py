from view_solution import show_list,update_key,enter_value,display
from model_solution import Program

program_list = show_list()
key = update_key()
value = enter_value()
dat = Program()
dat.get_list(program_list)
result = dat.update_list_key(program_list,key,value)
display(result)