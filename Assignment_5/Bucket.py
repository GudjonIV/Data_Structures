# Author: Guðjón Ingi Valdimarsson
# Date: 20.03.2020

class ItemExistsException(Exception):
    pass

class NotFoundException(Exception):
    pass

class Bucket():
    class _Node():
        def __init__(self, key=None, data=None, next=None):
            self.key = key
            self.data = data
            self.next = next

    def __init__(self):
        self.size = 0
        self.head = self._Node()
    
    def insert(self, key, data):
        if self.contains(key):
            raise ItemExistsException()
        self.head.next = self._Node(key, data, self.head.next)
        self.size += 1
    
    def update(self, key, data):
        node = self._find(key)
        node.data = data

    def _find(self, key, removeBool=False):
        walker = self.head.next
        prevNode = self.head    # Used for remove function to have a reference to the previous node
        while walker != None:
            if walker.key == key:
                if removeBool:
                    return (walker, prevNode)
                return walker
            walker = walker.next
            prevNode = prevNode.next
        raise NotFoundException()

    def find(self, key):
        return self._find(key).data

    def contains(self, key):
        try:
            self._find(key)
            return True
        except NotFoundException:
            return False

    def remove(self, key):
        node, prevNode = self._find(key, True)
        prevNode.next = node.next
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


# ---------- Not crucial to assignment ----------
    def __iter__(self):
        walker = self.head.next
        while walker != None:
            yield (walker.key, walker.data)
            walker = walker.next

    def __str__(self):
        ret_str = ""
        for item in self:
            ret_str += "({}: {}), ".format(item[0], item[1])
        return ret_str.strip(", ")

if __name__ == "__main__":
    buc = Bucket()
    for x in range(10):
        buc.insert(x, "value")
    print (buc)
    print (len(buc))
    buc.update(5, "not value")
    print (buc)
    buc[5] = "Val"
    buc[10] = "value"
    print (buc)
    buc.remove(10)
    print (buc)
    print (buc.find(4))
    print (buc[4])
    for item in buc:
        print (item)
