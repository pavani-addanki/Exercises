
class Person:
    def __init__(self,name,age,spouse = None,children = []):
        self.name = name
        self.age = age
        self.spouse = spouse
        self.children = children

class Child(Person):
    def __init__(self,name,age,spouse = None,children = [],parents =[]):
        super().__init__(name,age,spouse,children)
        self.parents = parents

jim = Person('Jim Brown',45)
suzy = Person('Suzy Brown',42)
jim.spouse = suzy
suzy.spouse = jim
martha = Child('Martha Brown',18,None,[],[jim,suzy])
jim.children = [martha]
suzy.children =[martha]

