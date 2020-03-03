# Author: Guðjón Ingi Valdimarsson
# Date: 03.03.2020

class BST():
    class _Node():
        def __init__(self, value=None, parent=None):
            self.value = value
            self.parent = parent
            self.left = None
            self.right = None

        def __str__(self):
            return self.value

    def __init__(self):
        self.root = self._Node()
        self.size = 0

    def _get_empty(self):
        return self.size == 0

    def _search_rec(self, node, value):
        if node.value == value:
            return node
        elif node.value > value:
            if node.left != None:
                return self._search_rec(node.left, value)
            return node
        else:
            if node.right != None:
                return self._search_rec(node.right, value)
        return node

    def search(self, value):
        if self._get_empty():
            return None
        return self._search_rec(self.root, str(value))

    def add(self, value):
        value = str(value)
        if self._get_empty():
            self.root = self._Node(value)
        else:
            node = self.search(value)
            if node.value == value:
                return print ("Value {} already exists".format(value))
            elif node.value < value:
                node.right = self._Node(value, node)
            else:
                node.left = self._Node(value, node)
        self.size += 1

    def _inorder(self, root):
        if root.left != None:
            self._inorder(root.left)
        print (root.value, end = " ")
        if root.right != None:
            self._inorder(root.right)

    def __str__(self):
        self._inorder(self.root)
        return ""

    def contains(self, value):
        node = self.search(value)
        return node.value == str(value)

if __name__ == "__main__":
    bst = BST()
    bst.add(5)
    bst.add(4)
    bst.add(3)
    bst.add(6)
    print (bst)
    bst.add(3)
    print (bst.contains(2))
    print (bst.contains(5))