# Author: Guðjón Ingi Valdimarsson

from my_array_deque import ArrayDeque
from my_linked_list import LinkedList

class Stack:
    def __init__(self, type):
        if type == "array":
            self.structure = ArrayDeque()
        elif type == "linked":
            self.structure = LinkedList()
        else:
            print ("Error unknown datastructure type")
    
    def push(self, data):
        self.structure.push_front(data)
    
    def pop(self):
        return self.structure.pop_front()
    
    def get_size(self):
        return self.structure.get_size()

if __name__ == "__main__":
    stack = Stack("array")
    print (stack.pop())
    stack.push(5)
    stack.push(6)
    stack.push(10)
    stack.push(8)
    stack.push(7)
    print (stack.pop())
    print (stack)
    print (stack.get_size())
