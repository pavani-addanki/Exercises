
def inventory_price(idict):
    total_price = 0

    for i,(j,k) in idict.items():
        total_price += j*k
    return total_price