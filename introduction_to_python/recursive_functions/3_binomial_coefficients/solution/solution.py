
def binomial_coefficient(n,k):
    if n < k:
        return 0
    if n == k or k == 0:
        return 1  
    if(n >= k):
        return binomial_coefficient(n-1, k-1) + binomial_coefficient(n-1, k)