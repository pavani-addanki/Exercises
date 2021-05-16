
def median_of_medians(lst):
    lst.sort()
    mid = len(lst) // 2
    result = (lst[mid]+lst[~mid])/2
    return result