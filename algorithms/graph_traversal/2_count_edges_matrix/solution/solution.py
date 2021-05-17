def count_edges(M):
    i,j,count=0,0,0
    for i in M:
        for j in i:
            if j==1:
                count=count+1
    return count