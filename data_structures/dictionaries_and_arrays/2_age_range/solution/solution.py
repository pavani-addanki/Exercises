
def remove_ages(pdict,x,y):
    pdict_new = {}
    for i,j in pdict.items():
        if(j>=x and j<=y):
            pdict_new[i] = j
    return pdict_new

