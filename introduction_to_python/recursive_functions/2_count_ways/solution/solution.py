
def count_ways(steps):
    if steps == 0 or steps == 1:
        return 1
    elif steps > 1:
        return count_ways(steps-1) + count_ways(steps-2)

"""
2
(1,1)(2)  -->2  --> 2-1+ 2-2
3
(1,1,1)(2,1)(1,2) --> 3   
4
(1,1,1,1)(1,1,2)(1,2,1)(2,1,1)(2,2)   --> 5
5
(1,1,1,1,1)(1,1,1,2)(1,1,2,1)

need to check steps == 0, output should not be one ?
"""