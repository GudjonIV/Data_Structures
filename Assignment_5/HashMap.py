# Author: Guðjón Ingi Valdimarsson
# Date: 20.03.2020

from Bucket import *

class HashMap():
    def __init__(self):
        self.capacity = 10
        self.size = 0
        self.arr = [Bucket() for _ in range(self.capacity)]
    
    def rebuild(self):
        if self.size >= self.capacity * 1.2:
            self.capacity *= 2
            temp_list = self.arr
            self.arr = [Bucket() for _ in range(self.capacity)]
            self.size = 0
            for bucket in temp_list:
                for item in bucket:
                    self.insert(item[0], item[1])
            
    def _get_index(self, key):
        return hash(key) % self.capacity

    def insert(self, key, data):
        if self.contains(key):
            raise ItemExistsException()
        self.rebuild()
        index = self._get_index(key)
        self.arr[index].insert(key, data)
        self.size += 1

    def update(self, key, data):
        self._find(key).data = data

    def _find(self, key): # Returns the node with given key
        index = self._get_index(key)
        return self.arr[index]._find(key)
    
    def find(self, key):
        return self._find(key).data

    def contains(self, key):
        try:
            self.find(key)
            return True
        except NotFoundException:
            return False

    def remove(self, key):
        index = self._get_index(key)
        self.arr[index].remove(key)
        self.size -= 1

    def __setitem__(self, key, data):
        try:
            self.update(key, data)
        except NotFoundException:
            self.insert(key, data)

    def __getitem__(self, key):
        return self.find(key)

    def __len__(self):
        return self.size

    def __iter__(self):
        for bucket in self.arr:
            for item in bucket:
                yield item
    
    def __str__(self):
        ret_str = ""
        for item in self:
            ret_str += "({}: {}), ".format(item[0], item[1])
        return ret_str.strip(", ")

if __name__ == "__main__":
    hm = HashMap()
    for x in range(13):
        hm.insert(x, "Value")
    for item in hm:
        print (item)
    hm.update(12, "Val")
    print (hm)
    print (len(hm))
    hm.remove(6)
    print (hm)
    print (len(hm))

    
