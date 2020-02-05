# Author: Guðjón Ingi Valdimarsson
# Date: 04.02.2020

class Empty(Exception):
    pass

class Stack():
    def __init__(self):
        self.capacity = 4
        self.arr = [None] * self.capacity
        self.size = 0

    def __check_empty(self):
        if self.size == 0:
            raise Empty("Stack is empty!")

    def __resize(self):
        if self.size == self.capacity:
            new_arr = [None] * (self.capacity * 2)
            for i in range(self.capacity):
                new_arr[i] = self.arr[i]
            self.arr = new_arr
            self.capacity = (self.capacity * 2)

    def pop(self):
        self.__check_empty()
        value = self.arr[self.size - 1]
        self.size -= 1
        return value

    def push(self, value):
        self.__resize()
        self.arr[self.size] = value
        self.size += 1

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print (stack.pop())
    print (stack.pop())
    print (stack.pop())


    