
def sort_siblings(sib_dict):    
    sib_dict = dict(sorted(sib_dict.items()))    
    sibList = sorted(sib_dict.items(), key= lambda x:x[1])    
    sortedDict = dict(sibList)     

    return sibList