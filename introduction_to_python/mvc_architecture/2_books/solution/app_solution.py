import json
from view_solution import show_list,retrive_book,display
from model_solution import Book

author = Book()
book_author_list = show_list()
n_book_list =json.dumps(book_author_list)
book_list = retrive_book()
book = retrive_book()
show = author.get_list(n_book_list)
data = author.retrive_book(show,book)
display(data)