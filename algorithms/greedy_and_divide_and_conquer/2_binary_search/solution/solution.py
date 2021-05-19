def binary_search(lst, x):  
    low = 0  
    high = len(lst) - 1  
    mid = 0  
  
    while low <= high:   
        mid = (high + low) // 2    
        
        if lst[mid] < x:  
            low = mid + 1    
        
        elif lst[mid] > x:  
            high = mid - 1  
        else:  
            return mid 

    return -1  
