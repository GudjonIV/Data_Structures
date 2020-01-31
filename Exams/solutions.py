# Author: Guðjón Ingi Valdimarsson
# Date: 30.01.2020

# Part B
class ValueCounter():
    def __init__(self):
        self.items_list = []    # Even though I don't use this at the moment it might be needed in another implementation
        self.items_dict = {}
    
    def set_items(self, lis):
        self.items_list = lis

        for value in lis:
            if value in self.items_dict:
                self.items_dict[value] += 1
            else:
                self.items_dict[value] = 1

    def print_count(self):      # O(n) time complexity where n is unique values
        for key, value in self.items_dict.items(): 
            print ("{}: {}".format(key, value))

# Part A
def count_values(lis):
    """ Takes in a list and prints unique values and their count """
    value_dict = {}
    for value in lis:       
        if value in value_dict:
            value_dict[value] += 1
        else:
            value_dict[value] = 1
    
    for key, value in value_dict.items():
        print ("{}: {}".format(key, value))

# Tests 
if __name__ == "__main__":
    listi = ["a", "b", "a", "d", "c", "d", "c", "c", "f", "b", "a", "a"]
    count_values(listi)

    print ("___________")

    value_counter = ValueCounter()
    value_counter.set_items(listi)
    value_counter.print_count()
