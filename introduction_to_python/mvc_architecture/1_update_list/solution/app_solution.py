from view_solution import ask_fruit, show_fruits
from model_solution import get_store,update_fruit

fruits = get_store()
show = show_fruits(fruits)
new_fruit = ask_fruit()
list_fruits = update_fruit(fruits,new_fruit)
#show_fruits(fruits)