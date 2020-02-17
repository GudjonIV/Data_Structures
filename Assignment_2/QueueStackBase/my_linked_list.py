# Author: Guðjón Ingi Valdimarsson

class LinkedList():
    class _Node():
        def __init__(self, data = None, next = None):
            self.data = data
            self.next = next
        
        def __str__(self):
            return str(self.data)
  
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __str__(self):
        ret_str = ""
        walk = self.head
        while walk != None:
            ret_str += str(walk.data) + " "
            walk = walk.next
        return ret_str.strip(" ")

    def push_back(self, data):
        node = self._Node(data)
        if self.head == None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1

    def push_front(self, data):
        node = self._Node(data, self.head)
        if self.head == None:
            self.tail = node
        self.head = node
        self.size += 1
    
    def pop_front(self):
        if self.head == None:
            return None
        value = self.head.data
        self.head = self.head.next
        self.size -= 1
        return value
    
    def get_size(self):
        return self.size

if __name__ == "__main__":
    link = LinkedList()
    link.push_front(2)
    link.push_front(5)
    link.push_back(10)
    print (link)