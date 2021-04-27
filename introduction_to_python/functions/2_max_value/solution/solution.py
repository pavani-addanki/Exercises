# Write your solution here

def max_val(a,b,c):
    if a>=b:
        if a>=c:
            return a
        else:
            return c
    elif b>=a:
        if b >= c:
            return b
        else:
            return c
    
