# Author: Guðjón Ingi Valdimarsson
# Date: 04.02.2020

class Queue():
    def __init__(self):
        self.capacity = 10
        self.arr = [None] * self.capacity
        self.size = 0
        self.front = 0

    def __str__(self):
        return str(self.arr)

    def __get_back(self):
        return (self.size + self.front) % self.capacity

    def __resize(self):
        if self.size == self.capacity:
            new_arr = [None] * (self.capacity * 2)
            walk = self.front
            for i in range(self.capacity):
                new_arr[i] = self.arr[walk]
                walk = (1 + walk) % self.capacity
            self.arr = new_arr
            self.capacity = (self.capacity * 2)
            self.front = 0
    
    def add(self, value):
        self.__resize()
        self.arr[self.__get_back()] = value
        self.size += 1

    def remove(self):
        value = self.arr[self.front]
        self.arr[self.front] = None
        self.size -= 1
        self.front += 1
        return value

if __name__ == "__main__":
    queue = Queue()
    queue.add(1)
    queue.add(2)
    queue.add(3)
    queue.add(4)
    queue.add(5)
    queue.add(7)
    queue.add(6)
    queue.add(10)
    queue.add(9)
    queue.add(11)
    print (queue.remove())
    print (queue.remove())
    queue.add(12)
    queue.add(13)
    queue.add(14)
    print (queue.remove())
    print (queue)
