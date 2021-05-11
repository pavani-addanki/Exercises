class Person:
    def __init__(self,name,age,spouse = None,children = []):
        self.name = name
        self.age = age
        self.spouse = spouse
        self.children = children

    def get_divorced(self):
        if self.spouse is not None: 
            spouse = self.spouse
            self.spouse = None
            spouse.spouse = None

class Child(Person):
    def __init__(self,name,age,spouse = None,children = [],parents =[]):
        super().__init__(name,age,spouse,children)
        self.parents = parents