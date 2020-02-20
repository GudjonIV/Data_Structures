# Author: Guðjón Ingi Valdimarsson

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)

class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.current = self.tail
        self.reverse_bool = False
        self.size = 0

    def __insert_between(self, data, before, after):
        new_node = Node(data, after, before)
        before.next = new_node
        after.prev = new_node
        self.size += 1

    def __remove_node(self, node):
        value = node.data
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return value

    def __str__(self):
        ret_str = ""
        if not self.reverse_bool:
            walker = self.head.next
            while walker.data != None:
                ret_str += str(walker) + " "
                walker = walker.next
        else:
            walker = self.tail.prev
            while walker.data != None:
                ret_str += str(walker) + " "
                walker = walker.prev
        return ret_str.strip()
    
    def __len__(self):
        return self.size

    def insert(self, value):
        if self.reverse_bool:
            self.__insert_between(value, self.current, self.current.next)
        else:
            self.__insert_between(value, self.current.prev, self.current)
        self.move_to_prev()
    
    def remove(self):
        if self.current != self.tail:
            self.__remove_node(self.current)
            self.move_to_next()
        
    def get_value(self):
        return self.current.data

    def move_to_next(self):
        if self.reverse_bool:
            if self.current != self.head.next:
                self.current = self.current.prev
        else:
            if self.current != self.tail:
                self.current = self.current.next

    def move_to_prev(self):
        if self.reverse_bool:
            if self.current != self.tail:
                self.current = self.current.next
        else:
            if self.current != self.head.next:
                self.current = self.current.prev

    def move_to_pos(self, position):
        if position < self.size:
            if self.reverse_bool: # Get new position if reverse is true
                position = self.size - 1 - position
            walker = self.head.next
            for _ in range(position):
                walker = walker.next
            self.current = walker   

    def remove_all(self, value):
        walker = self.head.next
        while walker != None:
            if value == walker.data:
                if walker == self.current:
                    self.move_to_pos(0)
                walker = walker.next
                self.__remove_node(walker.prev)
            else:
                walker = walker.next
    
    def reverse(self):
        self.reverse_bool = True
    
    def sort(self):
        pivot = self.head.next.next
        while pivot.next != None:
            walker = pivot
            while walker != self.head.next and walker.data < walker.prev.data:
                temp = walker.data
                walker.data = walker.prev.data
                walker = walker.prev
                walker.data = temp
            pivot = pivot.next
            
if __name__ == "__main__":
    dll = DLL()
    dll.insert(5)
    dll.insert(9)
    dll.insert(10)
    print (dll)
    dll.remove()
    print (dll)
    print (dll.get_value())
    dll.remove()
    dll.remove()
    dll.remove()
    dll.insert(15)
    dll.insert(6)
    dll.insert(8)
    dll.insert(7)
    dll.move_to_pos(2)
    dll.insert(8)
    dll.insert(17)
    print (dll)
    dll.remove_all(8)
    print (dll)
    dll.reverse()
    print (dll)
    dll.insert(9)
    dll.insert(10)
    dll.insert(8)
    print (dll)
    dll.sort()
    print (dll)