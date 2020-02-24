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
    
    def __get_next(self, node):
        if node == None:
            return None
        if self.reverse_bool:
            return node.prev
        else:
            return node.next
    
    def __get_prev(self, node):
        if node == None:
            return None
        if self.reverse_bool:
            return node.next
        else:
            return node.prev

    def __str__(self):
        ret_str = ""
        walker = self.__get_next(self.head)
        while walker.data != None:
            ret_str += str(walker) + " "
            walker = self.__get_next(walker)
        return ret_str
    
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
            self.current = self.__get_next(self.current)
        
    def get_value(self):
        return self.current.data

    def move_to_next(self):
        if self.current != self.tail:
            self.current = self.__get_next(self.current)

    def move_to_prev(self):
        if self.current != self.__get_next(self.head):
            self.current = self.__get_prev(self.current)

    def move_to_pos(self, position):
        if position <= self.size and position >= 0:
            if self.reverse_bool: # Get new position if reverse is true
                position = self.size - 1 - position
            walker = self.__get_next(self.head)
            for _ in range(position):
                walker = self.__get_next(walker)
            self.current = walker   

    def remove_all(self, value):
        current_bool = False
        walker = self.__get_next(self.head)
        while walker != None:
            if str(value) == str(walker.data):
                if walker == self.current:
                    current_bool = True
                walker = self.__get_next(walker)
                self.__remove_node(self.__get_prev(walker))
            else:
                walker = self.__get_next(walker)
        if current_bool:
            self.current = self.__get_next(self.head)
    
    def reverse(self):
        self.reverse_bool = not self.reverse_bool
        temp_head = self.head
        self.head = self.tail
        self.tail = temp_head
        self.current = self.__get_next(self.head)
    
    def sort(self):
        pivot = self.__get_next(self.__get_next(self.head))
        while self.__get_next(pivot) != None:
            walker = pivot
            while walker != self.__get_next(self.head) and walker.data < self.__get_prev(walker).data:
                temp = walker.data
                walker.data = self.__get_prev(walker).data
                walker = self.__get_prev(walker)
                walker.data = temp
            pivot = self.__get_next(pivot)
        self.current = self.__get_next(self.head)
            
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
    dll.reverse()
    print (dll)
    dll.sort()
    print (dll)
    dll.reverse()
    print (dll)
    dll.sort()
    print (dll)
    dll1 = DLL()
    dll1.insert("A")
    dll1.insert("C")
    dll1.insert("C")
    dll1.insert("B")
    dll1.insert("C")
    dll1.reverse()
    dll1.move_to_pos(0)
    dll1.move_to_pos(1)
    print (dll1)
    dll1.remove_all("C")
    print (dll1)