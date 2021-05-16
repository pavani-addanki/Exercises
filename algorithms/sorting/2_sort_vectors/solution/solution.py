from math import sqrt

def sort_vectors(vector_lst):
    final_vec_lst = list()
    dict_out = dict()
    for i in vector_lst:
        ((x1,y1),(x2,y2)) = i
        mag = sqrt((x2-x1)**2+(y2-y1)**2)
        dict_out[i] = mag
    
    sortVeclist = sorted(dict_out.items(), key=lambda x:x[1])    
    sortdict = dict(sortVeclist)
    
    for i in sortdict:
        final_vec_lst.append(i)    
    
    return final_vec_lst
