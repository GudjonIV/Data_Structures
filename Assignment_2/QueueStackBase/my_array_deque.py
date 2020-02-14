# Author: Guðjón Ingi Valdimarsson

class ArrayDeque():
    def __init__(self):
        self.capacity = 4
        self.arr = [None] * self.capacity
        self.size = 0
        self.front = 0

    def __str__(self):
        ret_str = ""
        walk = self.front
        for _ in range(self.size):
            ret_str += str(self.arr[walk]) + " "
            walk = (1 + walk) % self.capacity
        return ret_str.strip(" ")

    def __get_back(self): # Returns where the next back index should be
        return (self.size + self.front) % self.capacity

    def __resize(self): # Resizes the array
        if self.size == self.capacity:
            new_arr = [None] * (self.capacity * 2)
            walk = self.front
            for i in range(self.capacity):
                new_arr[i] = self.arr[walk]
                walk = (1 + walk) % self.capacity
            self.arr = new_arr
            self.capacity = (self.capacity * 2)
            self.front = 0
    
    def push_back(self, value):
        self.__resize()
        self.arr[self.__get_back()] = value
        self.size += 1

    def push_front(self, value):
        self.__resize()
        index = (self.front - 1) % self.capacity
        self.arr[index] = value
        self.front = index
        self.size += 1

    def pop_front(self):
        value = self.arr[self.front]
        self.arr[self.front] = None
        self.front = (self.front + 1) % self.capacity
        if self.size != 0:
            self.size -= 1
        return value
    
    def pop_back(self):
        value = self.arr[self.__get_back() - 1]
        self.arr[self.__get_back() - 1] = None
        if self.size != 0:
            self.size -= 1
        return value
    
    def get_size(self):
        return self.size

if __name__ == "__main__":
    deq = ArrayDeque()
    print (deq)
    print (deq.pop_back())
    deq.push_front(5)
    print (deq)
    deq.push_back(10)
    print (deq)
    deq.pop_back()
    print (deq)
    deq.push_front(7)
    deq.push_front(10)
    deq.push_front(3)
    print (deq)
    deq.push_back(8)
    print (deq)
    print (deq.get_size())
