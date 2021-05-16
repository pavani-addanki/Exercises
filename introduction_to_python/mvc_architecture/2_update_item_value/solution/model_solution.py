class Program:

    def __init__(self,program_list ={}):
        self.program_list = program_list

    def get_list(self,program_list):
        for k,v in self.program_list.items():
            return k,v

    def update_list_key(self,program_list,key,value):
        new_list = self.program_list.update({key:value})
        return new_list