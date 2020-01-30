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
        self.a_list = [0] * self.capacity

    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        return_string = ""
        for index in range(self.size):
            return_string += str(self.a_list[index]) + ", "
        return return_string.strip(", ")

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        #self.resize()
        for index in range(self.size, 0, -1):
            self.a_list[index + 1] = self.a_list[index]
        self.a_list[0] = value
        self.size += 1


            

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        pass

    #Time complexity: O(1) - constant time
    def append(self, value):
        pass

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        pass

    #Time complexity: O(1) - constant time
    def get_first(self):
        pass

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        pass

    #Time complexity: O(1) - constant time
    def get_last(self):
        pass

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        pass

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        pass

    #Time complexity: O(1) - constant time
    def clear(self):
        pass

    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        pass

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        pass

    #Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):
        pass


if __name__ == "__main__":
    arr_lis = ArrayList()
    print(str(arr_lis))
    arr_lis.prepend(1)
    arr_lis.prepend(2)
    arr_lis.prepend(3)
    print(str(arr_lis))
