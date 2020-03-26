# Author: Guðjón Ingi Valdimarsson
# Date: 20.03.2020

class MyHashableKey():
    def __init__(self, integer, string):
        self.integer = integer
        self.string = string
    
    def __eq__(self, other):
        return (self.integer, self.string) == (other.integer, other.string) and isinstance(other, MyHashableKey)
    
    def __hash__(self):
        a = 37
        ret = -self.integer
        for c in self.string:
            ret += a * ord(c)
        return abs(ret - 1)


if __name__ == "__main__":
    k1 = MyHashableKey(1, "one")
    print(hash(k1))
    k2a = MyHashableKey(2, "two")
    print(hash(k2a))
    k2b = MyHashableKey(2, "two")
    print(hash(k2b))
    print(k1 == k2a)
    print(k2a == k2b)