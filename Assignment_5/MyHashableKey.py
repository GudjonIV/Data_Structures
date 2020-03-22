# Author: Guðjón Ingi Valdimarsson
# Date: 20.03.2020

class MyHashableKey():
    def __init__(self, integer, string):
        self.integer = integer
        self.string = string
    
    def __eq__(self, other):
        return (self.integer, self.string) == (other.integer, other.string) and isinstance(other, MyHashableKey)
    
    def __hash__(self):
        a = 41
        ret = self.integer
        #string = string[5:] + string[:5]
        for index, c in enumerate(self.string):
            ret += (a**index) * ord(c)
        return ret


if __name__ == "__main__":
    k1 = MyHashableKey(1, "one")
    print(hash(k1))
    k2a = MyHashableKey(2, "two")
    print(hash(k2a))
    k2b = MyHashableKey(2, "two")
    print(hash(k2b))
    print(k1 == k2a)
    print(k2a == k2b)