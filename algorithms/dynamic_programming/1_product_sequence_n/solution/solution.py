
def product_sequence_n(n):
    if(n == 1):
        return 1
    elif(n == 2):
        return 2
    elif(n > 1):
        n = n * product_sequence_n(n-2)
    return n

