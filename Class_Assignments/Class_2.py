import random
# Class 2: Time complexity and list arrays

# 1. Power

def power(base, n):                 # Time complexity: O(n)
    total = 1                       # O(1)
    for _ in range(n):              # O(n)
        total = total * base        # O(1)
    return total                    # O(1)

"""
print (power(2, 2))
print (power(2, 1))
print (power(2, 5))
"""

# 2. Multiplication of positive integers

def mult(num_1, n):     # Time complexity: O(n)
    total = 0           # O(1)
    for _ in range(n):  # O(n)
        total += num_1  # O(1)
    return total        # O(1)

"""
print (mult(2, 2))
print (mult(20, 10))
print (mult(2, 5))
print (mult(5, 2))
"""

# 3. Random number insertion

def rand(n):                                # Time complexity: O(n)
    lis = [0] * n                           # O(1)
    for i in range(len(lis)):               # O(n)
        rand_int = random.randint(1, 6)     # O(1)
        lis[i] = rand_int                   # O(1)
    return lis                              # O(1)

"""
print (rand(10))
print (rand(30))
print (rand(20))
"""

# 4. Print your list to the screen

def prin(listi):                            # Time complexity: O(n), n = Len(list)
    for index, value in enumerate(listi):   # O(n)
        if index != len(listi) - 1:         # O(1)
            print (value, end=", ")         # O(1)
        else:                               # O(n)
            print (value)                   # O(1)

"""
listi = [1, 2, 3, 4, 5]
prin(listi)
"""

# 5. Increase random index

def inc(lis):                               # Time complexity: O(1)
    n = len(lis)                            # O(1)
    index = random.randint(0, n-1)          # O(1)
    lis[index] = lis[index] + 1             # O(1)
    return lis                              # O(1)

"""
listi = [1, 2, 3, 4, 5, 6]
print (inc(listi))
"""

# 6. Switch items in list

def switch_lis(listi, location = None):                # Time complexity: O(1)


    if not location:
        location = random.randint(0, len(listi) - 1)

    value_1 = listi[location]
    if location != 0:
        value_2 = listi[location - 1]
        listi[location] = value_2
        listi[location - 1] = value_1
    else:
        value_2 = listi[location + 1]
        listi[location] = value_2
        listi[location + 1] = value_1
    return listi

"""
listi = []
for _ in range(10):
    integer = random.randint(0, 10)
    listi.append(integer)

print (listi)
switch_lis(listi, 5)
print (listi)
"""

# 7. Ordered insertion

def ordered_insertion(listi, number):           # Time complexity: O(n^2)
    old = 0                                     # O(1)
    for index, value in enumerate(listi):       # O(n)
        if value >= number and old < number:    # O(1)
            listi.insert(index, number)         # O(n)
            old = number                        # O(1)
            break                               # O(1)
        old = value                             # O(1)
    if old < number:                            # O(1)
        listi.append(number)                    # O(1)
    return listi                                # O(1)

def better_ordered(listi, number):              # Time complexity: O(nLog(n))
    listi.append(number)                        # O(1)
    listi = sorted(listi)                       # O(nLog(n))
    return listi                                # O(1)

"""
listi = [1, 2, 3, 4, 5, 6, 7]
print (ordered_insertion(listi, 11))
"""

# 8. Combined insertion and ordering

def combined_insertion(listi):                                  # Time complexity: O(n^3)
    ordered_list = []                               
    for value in listi:                                         # O(n)
        ordered_list = ordered_insertion(ordered_list, value)   # O(n^2)
    return ordered_list

random_list = []
for value in range(100):
    rand_int = random.randint(1, 10)
    random_list.append(rand_int)

print (random_list)
print (combined_insertion(random_list))


