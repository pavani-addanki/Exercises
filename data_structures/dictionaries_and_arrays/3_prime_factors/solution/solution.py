def prime_factors(n):
    p_list = []

    i = 1
    while(i <= n):
        count = 0
        if(n % i == 0):
            j = 1
            while(j <= i):
                if(i % j == 0):
                    count = count + 1
                j = j + 1

            if (count <= 2):                       # for 1, count=1 so included <
                p_list.append(i)
        i = i + 1
    return p_list
            
        
#     return l1

#     for j in range(1,len(l1)+1):
#         print("in 2nd loop")
#         count = 0
#         print(l1[j])
#         if(l1[j] % j == 0):
#             count += 1
            
            
            
#             print(f"m value is {m}")
#             for i in range(1,m+1):
#                 if m % i == 0:
#                     p_count += 1
#             if(p_count <= 2 ):
#                 p_list.append(m)
#     return p_list

#print(prime_factors(13)) 
#print(prime_factors(10))