
def count_even(*args):
    evenCount = 0
    for n in args:
        if(n % 2 == 0):
            evenCount = evenCount+1
    return evenCount