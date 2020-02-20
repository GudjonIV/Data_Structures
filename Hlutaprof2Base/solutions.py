# Author: Guðjón Ingi Valdimarsson
# Date: 20.02.2020

class SLL_Node:
    # THIS IMPLEMENTATION OF SINGLY-LINKED LIST NODE
    # MUST BE USED UNCHANGED, FOR TESTING PURPOSES
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    def __str__(self):
        ret_str = ""
        node = self
        while node != None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str


class DLL_List:
    class _Node():
        def __init__(self, data = None, prev = None, next = None):
            self.data = data
            self.prev = prev
            self.next = next
        
        def __str__(self):
            return str(self.data)

    def __init__(self):
        self.head = self._Node()
        self.tail = self._Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def build_list(self, lis):
        for value in lis:
            new_node = self._Node(value, self.tail.prev, self.tail)
            new_node.prev.next = new_node
            self.tail.prev = new_node
    
    def print(self, backwards = False):
        ret_str = ""
        if not backwards:
            walker = self.head.next
            while walker.data != None:
                ret_str += str(walker) + " "
                walker = walker.next
        else:
            walker = self.tail.prev
            while walker.data != None:
                ret_str += str(walker) + " "
                walker = walker.prev
        print (ret_str.strip())
    
    def cointains(self, val):
        walker = self.head.next
        while walker != None:
            if str(walker) == str(val):
                return True
            walker = walker.next
        return False


def ordered_rec(head, ascending = True):
    if head.next == None:
        return True
    if ascending:
        if head.data <= head.next.data:
            return ordered_rec(head.next)
        else:
            return False
    else:
        if head.data >= head.next.data:
            return ordered_rec(head.next, False)
        else:
            return False

def is_ordered(head):
    if head == None or head.next == None: # Check if head is none or 1 item
        return True
    if head.data < head.next.data: # Check if list should be checked in ascending order
        return ordered_rec(head)
    elif head.data > head.next.data: # Check if list should be checked in descending order
        return ordered_rec(head, False)
    else:                            # If two ajecent nodes have the same value
        return is_ordered(head.next)


if __name__ == "__main__":
    dll = DLL_List()
    dll.build_list([2, 6, 3, 6, 2, 8, 9])
    dll.print()
    dll.print(True)
    print ("6: " + str(dll.cointains(6)) + " 7: " + str(dll.cointains(7)))
    print ("\n-------------------\n")
    print("Singly-linked node example:")
    head = SLL_Node(1, SLL_Node(2, SLL_Node(3, SLL_Node(4, SLL_Node(5)))))
    print(str(head))
    print (is_ordered(head))
    head1 = SLL_Node(5, SLL_Node(4, SLL_Node(3, SLL_Node(2, SLL_Node(1)))))
    print ("\nDescending list")
    print (str(head1))
    print (is_ordered(head1))
    print ("\nUnordered list")
    head2 = SLL_Node(5, SLL_Node(6, SLL_Node(3, SLL_Node(9, SLL_Node(1)))))
    print (str(head2))
    print (is_ordered(head2))
    print ("\nEmpty list")
    print (is_ordered(None))
    print("\nOne item")
    head3 = SLL_Node(1)
    print (str(head3))
    print (is_ordered(head3))

