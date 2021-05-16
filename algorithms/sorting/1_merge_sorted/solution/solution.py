
def merge_sorted(lst1,lst2):
    new_lst = list()
    if lst1:
        for i in lst1:
            new_lst.append(i)
    if lst2:
        for i in lst2:
            new_lst.append(i)    
    if new_lst:
        new_lst.sort()

    return new_lst