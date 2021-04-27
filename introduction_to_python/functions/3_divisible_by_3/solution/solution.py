# Write your code here

def divisible_by_3(*args):
    opList = []
    for n in args:
        if(n % 3 ==0):
            opList.append(n)
    return opList

