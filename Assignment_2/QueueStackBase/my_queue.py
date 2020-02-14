# Author: Guðjón Ingi Valdimarsson

from my_array_deque import ArrayDeque
from my_linked_list import LinkedList

class Queue:
    def __init__(self, type):
        if type == "array":
            self.structure = ArrayDeque()
        elif type == "linked":
            self.structure = LinkedList()
        else:
            print ("Error unknown datastructure type")

    def add(self, data):
        self.structure.push_back(data)

    def remove(self):
        return self.structure.pop_front()

    def get_size(self):
        return self.structure.get_size()

if __name__ == "__main__":
    queue = Queue("array")
    print (queue.remove())
    queue.add(5)
    queue.add(7)
    queue.add(10)
    queue.add(1)
    queue.add(6)
    print (queue.remove())
    print (queue.remove())
