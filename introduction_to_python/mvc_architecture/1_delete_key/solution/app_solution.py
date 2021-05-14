from view_solution import delete_key,display
from model_solution import dele_key
movie_list = delete_key()
key = delete_key()
data = dele_key()
data.get_list(movie_list)
final_list = data.del_list_key(movie_list,key)
display(final_list)