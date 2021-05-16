class Create_File:

    def __init__(self, file_name, content):
        self.file_name = file_name
        self.content = content

    def create(self):
        with open(self.file_name, "w") as f:
            return None

    def write(self):
        try:
            with open(self.file_name, "a") as f:
                f.write(self.content)
                return True
        except:
            return False
            

    def read(self):
        with open(self.file_name, "r") as f:
            result = f.read()
            return result