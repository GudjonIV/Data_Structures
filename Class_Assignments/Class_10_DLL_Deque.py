# Author: Guðjón Ingi Valdimarssonn
# Date: 11.02.2020

from Class_10_DLL import DLL

class DLL_Deque(DLL):
    def __init__(self):
        self.head = self._Node()
        self.tail = self._Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def push_front(self, data):
        self._insert_between(data, self.head, self.head.next)

    def push_back(self, data):
        self._insert_between(data, self.tail.prev, self.tail)

    def pop_front(self):
        self._remove_node(self.head.next)

    def pop_back(self):
        self._remove_node(self.tail.prev)

    def get_front(self):
        return self.head.next.data

    def get_back(self):
        return self.tail.prev.data

    def __str__(self):
        return str(self.head.next)

    def print_backwards(self):
        ret_str = ""
        walker = self.tail.prev
        while walker != self.head:
            ret_str += str(walker.data) + ", "
            walker = walker.prev
        print (ret_str.strip(", "))

if __name__ == "__main__":
    dll_deque = DLL_Deque()
    dll_deque.push_front(1)
    dll_deque.push_front(2)
    dll_deque.push_front(3)
    dll_deque.push_front(4)
    dll_deque.push_front(5)
    print (dll_deque)
    dll_deque.print_backwards()
        























"""
class DLL():
    class _Node():
        def __init__(self, data=None, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

        def __str__(self):
            return "{}, {}".format(self.data, self.next).strip(", None, None")

    def __init__(self):
        self.head = self._Node()
        self.tail = self._Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def push_front(self, data):
        new_node = self._Node(data, self.head.next, self.head)
        self.head.next.prev = new_node
        self.head.next = new_node
        if self.tail.prev == self.head:
            self.tail.prev = new_node

    def push_back(self, data):
        new_node = self._Node(data, self.tail, self.tail.prev)
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        if self.head.next == self.tail:
            self.head.next = new_node

    def pop_front(self):
        value = self.head.next.data
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        return value

    def pop_back(self):
        value = self.tail.prev.data
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        return value
    
    def get_front(self):
        return self.head.next.data

    def get_back(self):
        return self.tail.prev.data

    def __str__(self):
        return str(self.head.next)
"""