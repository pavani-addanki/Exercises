class Book:
    
    def __init__(self,book_author_list={}):
        self.book_author_list = book_author_list
        

    def __str__(self,book_author_list):
        print(book_author_list)
        
    def get_list(self,book_author_list):
        for k,v in self.book_author_list.items():
            return k,v

    def retrive_book(self,book_author_list,book):
        for book in self.book_author_list:
            return book_author_list[book]