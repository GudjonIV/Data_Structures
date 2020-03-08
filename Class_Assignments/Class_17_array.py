# Author: Guðjón Ingi Valdimarsson
# Date: 05.03.2020

class PriorityQueueArr():
    class _Item():
        def __init__(self, value, priority):
            self.value = value
            self.priority = priority

        def __lt__(self, other):
            return self.priority < other.priority

        def __gt__(self, other):
            return not self < other

    def __init__(self):
        self.capacity = 4
        self.arr = [0] * self.capacity
        self.size = 0
    
    def _resize(self):
        if self.size == self.capacity:
            self.capacity = 2 * self.capacity
            new_arr = [0] * self.capacity
            for index in range(self.size):
                new_arr[index] = self.arr[index]
            self.arr = new_arr

    def add(self, value, priority):
        new_item = self._Item(value, priority)
        if self.size == 0:
            self.arr[0] = new_item
        else:
            self._resize()
            self.arr[self.size] = new_item
            for index in range(self.size, 0, -1):
                if self.arr[index] < self.arr[index - 1]:
                    temp = self.arr[index]
                    self.arr[index] = self.arr[index - 1]
                    self.arr[index - 1] = temp
        self.size += 1
    
    def remove(self):
        value = self.arr[0]
        for index in range(self.size - 1):
            self.arr[index] = self.arr[index + 1]
        self.arr[self.size - 1] = 0
        self.size -= 1
        return value

if __name__ == "__main__":
    pri = PriorityQueueArr()
    pri.add(5, 1)
    pri.add(4, 2)
    pri.add(17, 2)
    pri.add(30, 0)
    print (pri.remove())
    print ("")
                    