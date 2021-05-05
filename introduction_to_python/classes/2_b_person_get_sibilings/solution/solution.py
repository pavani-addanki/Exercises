class Person:
    def __init__(self, name : str, age: int, spouse: None, children:[]):
        self.name = name
        self.age = age
        self.spouse = spouse
        self.children = children

class Child(Person):
    def __init__(self, name, age, spouse, children, parents:[]):
        super().__init__(name,age,spouse,children)
        self.parents= parents
    
    def get_siblings(self):
        parents_list = self.parents
        # return parents_list
        child_dict = {}
        child_list = []
        for i in parents_list:
            for x in i.children:
                if x.name != self.name:
                    child_dict[x.name] = x.age
        stu_tuple = sorted(child_dict.items(), key=lambda x: x[1])
        print(stu_tuple)
        for i in stu_tuple:
            child_list.append(i[0])
        return child_list