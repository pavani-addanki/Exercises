def election_winner(clst):
    e_dict = {}
    clst.sort()
    for i in clst:
            if clst.count(i)>0:
                e_dict[i] = clst.count(i)
    e_key = max(e_dict, key = e_dict.get)
    return e_key