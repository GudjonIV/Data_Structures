# Author: Guðjón Ingi Valdimarsson
# Date: 17.03.2020

from random import Random

class HashableKey():
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __hash__(self):
        a = 41
        ret = 0
        for index, c in enumerate(str(self.key)):
            ret += (a**index) * ord(c)
        return ret

    def __eq__(self, other):
        if isinstance(other, HashableKey):
            return self.key == other.key
        return False

if __name__ == "__main__":
    rand = Random()
    lis_size = 10
    lis = [0] * lis_size
    for _ in range(10000):
        key = HashableKey(rand.randint(0, 200), "Value")
        index = hash(key) % lis_size
        lis[index] += 1
    print (lis)
    difference = max(lis) - min(lis)
    ratio = difference / max(lis)
    print ("List difference:",  )
    print ("Distibution ratio:", ratio)

print ()