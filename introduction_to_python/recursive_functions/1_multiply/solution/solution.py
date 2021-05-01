
def multiply(a,b):
    if a == 0 or b == 0:
        return 0
    elif(a > 0 and b > 0):
        return a + multiply(a,b-1)


"""
4*7
4+ 4*6
4+4+ 4*5
4+4+4+ 4*4
4+4+4+4+ 4*3
4+4+4+4+4+ 4*2
4+4+4+4+4+4+ 4*1
4+4+4+4+4+4+4+ 4*0
"""



