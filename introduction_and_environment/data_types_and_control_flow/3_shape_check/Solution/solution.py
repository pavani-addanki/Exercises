# Code your solution here

g_lst = []
shapes_dict = {3:'Triangle', 4:'Quadrilateral' , 5:'Pentagon' , 6:'Hexagon', 7:'Heptagon', 8:'Octagon', 9:'Nonagon'}

while True:
    g_int = int(input('Enter input'))
    if (g_int in shapes_dict):
        g_lst.append(shapes_dict[g_int]) 
    else:
        break