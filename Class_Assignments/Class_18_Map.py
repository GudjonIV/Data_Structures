# Author: Guðjón Ingi Valdimarsson
# Date: 10.03.2020

from random import Random

class Map():
    class _Item():
        def __init__(self, key, value):
            self.key = key
            self.value = value

        def getItems(self):
            return (self.key, self.value)

        def getKey(self):
            return self.key
        
        def getValue(self):
            return self.value
        
        def __lt__(self, other):
            return self.key < other.key
        
        def __gt__(self, other):
            return self.key > other.key
        
        def __repr__(self):
            return str(self.key) + ":" + str(self.value)

        
    def __init__(self):
        self.capacity = 8
        self.size = 0
        self.arr = [None] * self.capacity

    def __len__(self):
        return self.size
        
    def __str__(self):
        return str(self.arr)

    def _resize(self):
        if self.capacity == self.size:
            self.capacity = self.capacity * 2
            new_arr = [None] * self.capacity
            for index in range(self.size):
                new_arr[index] = self.arr[index]
            self.arr = new_arr

    def _insert_sort(self, k, v):
        self._resize()
        self.arr[self.size] = self._Item(k, v)
        for index in range(self.size, 0, -1):
            if self.arr[index] < self.arr[index - 1]:
                temp = self.arr[index - 1]
                self.arr[index - 1] = self.arr[index]
                self.arr[index] = temp
            else:
                break
        self.size += 1

    def insert(self, k, v):
        try:
            self.find(k)
            print ("Key already exists")
        except KeyError:
            self._insert_sort(k, v)

    def _find(self, k, remove=False):
        for index in range(self.size):
            if self.arr[index].getKey() == k:
                if remove:
                    self.arr[index] = None
                    return index
                return self.arr[index]
        raise KeyError("Key: {} not found".format(k))

    def find(self, k):
        return self._find(k).getValue()

    def update(self, k, v):
        item = self._find(k)
        item.value = v
    
    def remove(self, k):
        item = self._find(k, True)
        for index in range(item, self.size):
            if index == self.capacity - 1:
                self.arr[index] == None
            else:
                self.arr[index] = self.arr[index + 1]
        print ("")


    
if __name__ == "__main__":
    rand = Random()
    map = Map()
    for _ in range(9):
        key = rand.randint(0, 15)
        map.insert(key, "S")
    map.insert(112, "S")
    print (map)
    #print (map.find(111))
    map.update(112, "ARG")
    print (map)
    map.remove(112)
    print (map)