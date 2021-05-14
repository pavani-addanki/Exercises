
def tribonacci(n):
    tr = 0
    if(n in [0,1]):
        return 0
    elif(n == 2):
        return 1
    elif(n >= 3):
        tr = tr + tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
    return tr



    #`T(0) = 0`, `T(1) = 0`, `T(2) = 1`, and `T(n) = T(n-1) + T(n-2) + T(n-3)` for `n>=3