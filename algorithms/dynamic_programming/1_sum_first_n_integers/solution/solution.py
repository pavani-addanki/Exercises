
def sum_first_n(n):
    sum_first = 0
    if(n>0):
        sum_first = n + sum_first_n(n-1)
    return sum_first
