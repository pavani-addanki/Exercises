def quick_sort(lst):
    quick_sort_helper(lst, 0, len(lst) - 1)
    return lst


def quick_sort_helper(lst, min_index, max_index):
    if min_index < max_index:
        """we are checking the len of list is > 1"""
        pivot_index = _partition(lst, min_index, max_index)
        quick_sort_helper(lst, min_index, pivot_index - 1)
        quick_sort_helper(lst, pivot_index + 1, max_index)
    else:
        return lst

def _partition(lst, min_index, max_index):
    """pivot index can be set to any index in the list.
    we select the pivot element as the element at the mid point"""
    pivot_index = (min_index + max_index) // 2
    print(pivot_index, lst)
    """we swap the pivot element with min index element, 
    so that the pivot element is at the min index""" 
    lst[min_index], lst[pivot_index] = lst[pivot_index], lst[min_index]
    pivot_index = min_index
    """then we loop through the list, if we find an element smaller than pivot element,
    we swap it to the left of the pivot"""
    for index in range(min_index, max_index + 1):
        if lst[index] < lst[pivot_index]:
            """three way swap"""
            lst[pivot_index], lst[index] = lst[index], lst[pivot_index]
            lst[pivot_index + 1], lst[index] = lst[index], lst[pivot_index + 1]
            pivot_index += 1
        print(lst)
    """at the end of the partition function the pivot element is at its correct position and 
    we split the list at the pivot element position to recursively call the same function
    on left and and right side of the pivot"""
    return pivot_index
