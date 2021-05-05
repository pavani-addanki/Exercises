class Person:
    def __init__(self,name,age,spouse = None,children = []):
        self.name = name
        self.age = age
        self.spouse = spouse
        self.children = children

    def give_birth(self,name):
        if self.spouse is not None:
            self.children.append(Child(name,0,None,[],[self,self.spouse]))
            self.spouse.children.append(Child(name,0,None,[],[self,self.spouse]))
        else:
            self.children.append(Child(name,0,None,[],[self]))

class Child(Person):
    def __init__(self,name,age,spouse = None,children = [],parents =[]):
        super().__init__(name,age,spouse,children)
        self.parents = parents