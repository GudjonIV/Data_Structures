# Author: Guðjón Ingi Valdimarsson
# Date: 11.02.2020

from Class_10_DLL import DLL

class DLL_PosList(DLL):
    def __init__(self):
        self.head = self._Node()
        self.tail = self._Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.curr = self.tail
        self.size = 0
    
    def __str__(self):
        return str(self.head.next)

    def insert(self, data):
        self._insert_between(data, self.curr.prev, self.curr)
        self.curr = self.curr.prev
        self.size += 1

    def get_size(self):
        return self.size

    def print_backwards(self):
        ret_str = ""
        walker = self.tail.prev
        while walker != self.head:
            ret_str += str(walker.data) + ", "
            walker = walker.prev
        print (ret_str.strip(", "))

    def move_to_next(self):
        if self.curr != self.tail:
            self.curr = self.curr.next

    def move_to_prev(self):
        if self.curr.prev != self.head:
            self.curr = self.curr.prev

    def get_value(self):
        return self.curr.data

    def remove(self):
        if self.curr != self.tail:
            self.move_to_next()
            self._remove_node(self.curr.prev)

if __name__ == "__main__":
    pos_lis = DLL_PosList()
    pos_lis.insert("A")
    pos_lis.insert("B")
    #pos_lis.move_to_next()
    pos_lis.insert("C")
    #pos_lis.move_to_prev()
    #pos_lis.insert("D")
    print (pos_lis)
    pos_lis.remove()
    print (pos_lis)
    pos_lis.remove()
    print (pos_lis)
    #pos_lis.print_backwards()
    #print (pos_lis.get_size())