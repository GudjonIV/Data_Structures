# Author: Guðjón Ingi Valdimarsson
# Date: 05.03.2020

class HeapPQ():
    class _Node():
        def __init__(self, value, priority, parent = None):
            self.value = value
            self.priority = priority
            self.parent = parent
            self.left = None
            self.right = None

        def __lt__(self, other):
            return self.value < other.value

        def __gt__(self, other):
            return self.value > other.value
        
        def __str__(self):
            return str((self.value, self.priority))

    def __init__(self):
        self.root = None
        self.last = None
        self.size = 0

    def _add_node(self, node, parent):
        if parent.left is None:
            parent.left = node
        else:
            parent.right = node
        node.parent = parent
        self.last = node

    def _check_right(self, node):
        if node == self.root:
            return self._get_left(node)
        elif node.parent.right == node:
            return self._check_right(node.parent)
        return False

    def _get_next(self):
        if self.last == self.root:
            return self.root

        elif self.last.parent.left == self.last:
            return self.last.parent

        check_right = self._check_right(self.last)
        if check_right:
            return check_right

        elif self.last.parent.right == self.last:
            top = self._get_top(self.last.parent)
            return self._get_left(top.parent.right)

    def _get_top(self, node):
        if node.parent.left == node or node.parent == None:
            return node
        elif node.parent.right == node:
            return self._get_top(node.parent)
    
    def _get_left(self, node):
        if node.left == None:
            return node
        return self._get_left(node.left)

    def add(self, value, priority):
        new_item = self._Node(value, priority)
        if not self.root:
            self.root = self.last = new_item
        else:
            next_node = self._get_next()
            self._add_node(new_item, next_node)

    def _upheap(self, node):
        


    def print_tree(self):
        print ("{:>60}".format(str(self.root)))
        print ("{:>40}{:>40}".format(str(self.root.left), str(self.root.right)))
        print ("{:>30}{:>20}{:>20}{:>20}".format(str(self.root.left.left), str(self.root.left.right), str(self.root.right.left), str(self.root.right.right)))

if __name__ == "__main__":
    heap = HeapPQ()
    heap.add("arg", 1)
    heap.add("arg", 5)
    heap.add("arg", 12)
    heap.add("arg", 3)
    heap.add("arg", 2)
    heap.add("arg", 10) 
    heap.add("arg", 7)
    heap.print_tree()
