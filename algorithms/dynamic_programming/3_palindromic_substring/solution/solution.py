
def longest_palindrome_substr(str):
    op_l = list()
    if(len(str) == 0):
        return 0
    elif(len(str) == 1):
        return 1
    else:
        for i in range(0,len(str)):
            for j in range(0,len(str)):
                #print(str[i:j])
                if is_palindrome(str[i:j]):
                    #print(len(str[i:])
                    op_l.append(len(str[i:j]))
        return max(op_l)

def is_palindrome(str):
    revStr = str[::-1]
    if(str == revStr):
        return True
    else:
        return False