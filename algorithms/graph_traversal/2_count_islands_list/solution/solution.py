def count_islands(M):
    count=0
    for i,j in M.items():
        if len(j)==0:
            count=count +1 
    return count