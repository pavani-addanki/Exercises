
def intersect_lists(lst1,lst2):
    int_list = []
    for i in lst1:
        for j in lst2:
            if(i == j):
                int_list.append(i)
    return int_list

