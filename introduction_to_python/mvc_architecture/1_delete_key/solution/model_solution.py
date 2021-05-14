class dele_key:

    def __init__(self,movie_list={}):
        self.movie_list = movie_list

    def get_list(self,movie_list):
        return self.movie_list.values()

    def del_list_key(self,movie_list,key):
        if key in self.movie_list.values():
            self.movie_list.pop(movie_list.key())