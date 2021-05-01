

def sum_array(num_list):
    if not num_list:
        return 0
    else:
        return num_list[0]+ sum_array(num_list[1:])
