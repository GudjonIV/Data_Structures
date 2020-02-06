# Author: Guðjón Ingi Valdimarsson
# Date: 06.02.2020

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
            ret_str += str(walk.data) + ", "
            walk = walk.next
        return ret_str.strip(", ")
    
    def _push_front(self, data):
        node = self._Node(data, self.head)
        if self.head == None:
            self.tail = node
        self.head = node
        self.size += 1
    
    def _push_back(self, data):
        node = self._Node(data)
        if self.head == None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1
    
    def _pop_front(self):
        value = self.head.data
        self.head = self.head.next
        self.size -= 1
        return value
    
    def _pop_back(self):
        value = self.tail.data
        walk = self.head
        while walk.next != self.tail:
            walk = walk.next
        self.tail = walk
        self.size -= 1
        return value
    
    def get_size(self):
        return self.size


class Stack(LinkedList):
    def push(self, data):
        self._push_front(data)

    def pop(self):
        return self._pop_front()
    
    def __str__(self):
        ret_str = "\n"
        walk = self.head
        while walk != None:
            ret_str += str(walk.data) + "\n"
            walk = walk.next
        return ret_str

class Queue(LinkedList):
    def push(self, data):
        self._push_back(data)

    def pop(self):
        return self._pop_front()


if __name__ == "__main__":
    # link = LinkedList()
    # link.push_front(1)
    # link.push_front(2)
    # link.push_back(5)
    # print (link.pop_front())
    # print (link)
    # print (link.pop_front())
    # print (link)
    s = Stack()
    s.push("a")
    s.push("b")
    print(s)
    print ("Returned:", s.pop())
    print(s)

    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    print (q)
    print (q.pop())
    print (q)
    print (q.get_size())