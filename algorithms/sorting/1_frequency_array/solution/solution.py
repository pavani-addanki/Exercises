
def frequency_array(lst):
    new_lst = list()
    if lst:
        lst_size = max(lst)        
        for item in range(0,lst_size+1):
            new_lst.append(lst.count(item))        
        return new_lst
    return lst