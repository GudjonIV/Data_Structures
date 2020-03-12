
class ItemExistsException(Exception):
    pass

class NotFoundException(Exception):
    pass

class Bucket():
    class _Node():
        def __init__(self, key, data, next=None):
            self.key = key
            self.data = data
            self.next = next

    def __init__(self):
        self.size = 0
        self.head = None
    
    def insert(self, key, data):
        if self.contains(key):
            raise ItemExistsException
    
    def update(self, key, data):
        if not self.contains(key):
            raise ItemExistsException

    def find(self, key, nodeBool=False):
        walker = self.head
        while walker != None:
            if walker.key == key:
                if nodeBool:    # If true returns the whole node
                    return walker
                else:           # Else returns the node data
                    return walker.data
            walker = walker.next
        raise NotFoundException

    def contains(self, key):
        pass

    def remove(self, key):
        pass

    def __setitem__(self, key, data):
        pass

    def __getitem__(self, key):
        pass

    def __len__(self):
        return self.size