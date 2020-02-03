# Student: Guðjón Ingi Valdimarsson
# Date. 03.02.2020

class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class NotOrdered(Exception):
    pass

class ArrayList:
    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.arr = [0] * self.capacity
        self.ordered_bool = True

    def __check_index(self, index):
        """ Function that checks if index is within bounds, raises index error if not """
        if index >= self.size or index < 0:
            raise IndexOutOfBounds()
    
    def __check_empty(self):
        """ Function that checks if array is empty, raises empty error if so """
        if self.size == 0:
            raise Empty()

    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        return_string = ""
        for index in range(self.size):
            return_string += str(self.arr[index]) + ", "
        return return_string.strip(", ")

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        self.resize()
        for i in range(self.size, 0, -1):
            self.arr[i] = self.arr[i - 1]
        self.arr[0] = value
        self.size += 1
        self.ordered_bool = False

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        if index == self.size:
            self.append(value)
        else:
            self.__check_index(index)
            self.resize()
            for i in range(self.size, index, -1):
                self.arr[i] = self.arr[i - 1]
            self.arr[index] = value
            self.size += 1
        self.ordered_bool = False    

    #Time complexity: O(1) - constant time
    def append(self, value):
        self.resize()
        self.arr[self.size] = value
        self.size += 1
        self.ordered_bool = False

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        self.__check_index(index)
        self.arr[index] = value
        self.ordered_bool = False

    #Time complexity: O(1) - constant time
    def get_first(self):
        self.__check_empty()
        return self.arr[0]

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        self.__check_index(index)
        return self.arr[index]

    #Time complexity: O(1) - constant time
    def get_last(self):
        self.__check_empty()
        return self.arr[self.size - 1]

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        if self.size == self.capacity:
            new_arr = [0] * (self.capacity * 2)
            for i in range(self.capacity):
                new_arr[i] = self.arr[i]
            self.arr = new_arr
            self.capacity = (self.capacity * 2)

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        self.__check_index(index)
        for i in range(index, self.size - 1):
            self.arr[i] = self.arr[i + 1]
        self.size -= 1
        self.ordered_bool = False


    #Time complexity: O(1) - constant time
    def clear(self):
        self.ordered_bool = True
        self.size = 0


# Sorting and searching:
    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        if self.ordered_bool:
            self.append(value)
            for i in range (self.size - 1, 0, - 1):
                if self.arr[i - 1] > self.arr[i]:
                    self.arr[i] = self.arr[i - 1]
                    self.arr[i - 1] = value
            self.ordered_bool = True    # Needed to reset change after append
        else:
            raise NotOrdered()

    def __linear_search(self, value):
        for i in range(self.size):
            if self.arr[i] == value:
                return i
        raise NotFound()

    def __binary_search(self, value, low = 0, high = None):
        if high == None:
            high = self.size
        if low > high:        
            raise NotFound()
        else:
            mid = (low + high) // 2
            if value == self.arr[mid]:
                return mid
            elif value < self.arr[mid]:
                return self.__binary_search(value, low, mid - 1)
            else:
                return self.__binary_search(value, mid + 1, high)
    
    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        if not self.ordered_bool:
            return self.__linear_search(value)
        else:
            return self.__binary_search(value)

    #Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):
        val_index = self.find(value)
        self.remove_at(val_index)

if __name__ == "__main__":
    arr_lis = ArrayList()
    arr_lis.insert_ordered(4)
    arr_lis.insert_ordered(1)
    arr_lis.insert_ordered(2)
    arr_lis.insert_ordered(3)
    arr_lis.insert_ordered(16)
    arr_lis.insert_ordered(1005)
    arr_lis.remove_value(3)
    arr_lis.insert(5, 5)
    print (arr_lis)
