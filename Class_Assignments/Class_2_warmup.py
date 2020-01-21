

# WARMUP

# O(1)
listi = [1, 5, 3, 2, 1]
listi.append(1)

# O(Log(n))
n = 100
i = 1
counter = 1
while (i < n):
    i *= 2
    counter += 1

print (counter)

# O(nLog(n))
listi = [1, 2, 4, 7, 3, 1, 2, 4]
sorted_list = sorted(listi)

# O(n^2)
for value in range(n):
    for value_2 in range(n):
        pass

# O(n^3)
for value in range(n):
    for value_2 in range(n):
        for value_3 in range(n):
            pass
    
# O(2^n)
def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print (fibonacci(40))
