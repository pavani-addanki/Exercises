
def power(a,b):
    if b == 0:
        return 1
    else:
        return a * power(a,b-1)

"""
2**5
2 * 2**4
2 * 2 * 2**3
2 * 2 * 2 * 2**2
2 * 2 * 2 * 2 * 2**1
2 * 2 * 2 * 2 * 2 * 2**0

"""