# Author: Guðjón Ingi Valdimarsson
# Date: 04.02.2020

class Deque():
    def __init__(self):
        self.capacity = 4
        self.arr = [None] * self.capacity
        self.size = 0
        self.front = 0

    def __str__(self):
        ret_str = ""
        walk = self.front
        for _ in range(self.size):
            ret_str += str(self.arr[walk]) + ", "
            walk = (1 + walk) % self.capacity
        return ret_str.strip(", ")

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
    
    def push_front(self, value):
        self.__resize()
        index = (self.front - 1) % self.capacity
        self.arr[index] = value
        self.front = index
        self.size += 1

    def push_back(self, value):
        self.__resize()
        self.arr[self.__get_back()] = value
        self.size += 1

    def pop_front(self):
        value = self.arr[self.front]
        self.arr[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value
    
    def pop_back(self):
        value = self.arr[self.__get_back() - 1]
        self.arr[self.__get_back() - 1] = None
        self.size -= 1
        return value


if __name__ == "__main__":
    deque = Deque()
    deque.push_back(1)
    deque.push_front(2)
    deque.push_back(3)
    deque.push_back(4)
    deque.push_back(7)
    print (deque)
    print (deque.pop_back())
    print (deque.pop_front())
    print (deque)