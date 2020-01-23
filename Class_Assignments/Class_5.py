# Author: Guðjón Ingi Valdimarsson
# Date: 23.01.2020

def len_str(n_str):
    if n_str == "":
        return 0
    return len_str(n_str[1:]) + 1

def lin_search(lis, value):
    if lis == []:
        return False
    if lis[-1] == value:
        return True
    return lin_search(lis[:-1], value)

def count_inst(lis, value):
    if lis == []:
        return 0
    elif lis[-1] == value:
        return count_inst(lis[:-1], value) + 1
    return count_inst(lis[:-1], value)

def dub_val(lis):
    if lis == []:
        return False
    elif count_inst(lis, lis[-1]) > 1:
        return True
    return dub_val(lis[:-1])

def remove_dub(lis):
    new_list = []
    if lis == []:
        new_list = []
    else:
        if lin_search(lis[1:], lis[0]):
            new_list = remove_dub(lis[1:])
        else:
            new_list = [lis[0]] + remove_dub(lis[1:])
    return new_list
        
def binary_search(lis, value, low=0, high=None):
    if high == None:
        high = len(lis)
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if value == lis[mid]:
            return True
        elif value < lis[mid]:
            return binary_search(lis, value, low, mid - 1)
        else:
            return binary_search(lis, value, mid + 1, high)    
            
    """
    prefix_bool = True
    for index, value in enumerate(prefix):
        if value == a_str[index]:
            prefix_bool = prefix_bool & True
        else:
            prefix_bool = prefix_bool & False
    return prefix_bool
    """

def is_substring(substring, a_str):
    if not a_str:
        return False

    if substring == a_str[:len_str(substring)]:
        return True
    else:
        if len_str(a_str) < len_str(substring):
            return False
        else:
            return is_substring(substring, a_str[1:])

def x_ish(a_str, x):
    if x == "":
        return True
    if is_substring(x[0], a_str):
        return x_ish(a_str, x[1:])
    else:
        return False

def palindrome(a_str):
    if len_str(a_str) == 1 or len_str(a_str) == 0:
        return True
    
    if a_str[0] == a_str[-1]:
        return palindrome(a_str[1:-1])
    return False
    

"""
print (len_str("asd"))
print (lin_search([1, 3, 4, 5, 6, 7], 3))
print (count_inst([1, 2, 3, 4, 5, 6, 7, 1], 1))
print (dub_val([1, 2, 3, 4, 5, 6, 7, 8]))
print (remove_dub([1, 2, 3, 4, 5, 5, 6, 8]))
print (binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 1))
print (is_substring("asd", "asasdf"))
print (x_ish("Gagnaskipan", "gnAsk"))
print (palindrome("asdsa"))
"""