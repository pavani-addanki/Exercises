
def paths_nth_stair(n):
    if n == 0 or n == 1:
        return 1
    elif n > 1:
        return paths_nth_stair(n-1) + paths_nth_stair(n-2)