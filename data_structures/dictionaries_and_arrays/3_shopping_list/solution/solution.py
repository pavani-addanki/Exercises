def cheapest_store(grocery_dict, shopping_list):
    total_cost_dict = dict()
    for grocery in grocery_dict:
        total_cost = 0
        total_cost_dict[grocery] = total_cost 
        for item in shopping_list:
            if item not in grocery_dict[grocery]:
                total_cost_dict[grocery] += 5
            else:
                total_cost_dict[grocery] +=  grocery_dict[grocery][item]
    sorted_total_cost_dict = dict()
    for k, v in sorted(total_cost_dict.items()):
        sorted_total_cost_dict[k] = v
    print(sorted_total_cost_dict)
    _cheapest_store = min(sorted_total_cost_dict, key=total_cost_dict.get)
    print(sorted_total_cost_dict)
    print(_cheapest_store)
    return _cheapest_store