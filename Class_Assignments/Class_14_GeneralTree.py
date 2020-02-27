# Author: Guðjón Ingi Valdimarsson
# Date: 25.02.2020

class GeneralTree():
    class _Node():
        def __init__(self, data):
            self.data = data
            self.child_list = []
        
        def populate(self, node):
            self.child_list.append(node)

    def __init__(self):
        self.root = None
        self.size = 0


    # ----- Populate tree -----
    def _populate_rec(self, level = 0):
        data_input = input()
        if data_input == "":
            return
        level += 1
        node = self._Node(data_input)
        while True:
            print (level * "  |" + " --:", end=" ")
            child_node = self._populate_rec(level)
            if child_node == None:
                break
            node.populate(child_node)
        return node

    def populate_tree(self):
        print ("ROOT:", end= " ")
        self.root = self._populate_rec()

    # ----- Preorder -----
    def _preorder_rec(self, root, level = 1):
        for node in root.child_list:
            print (level * "  |" + " --:", node.data)
            self._preorder_rec(node, level + 1)

    def print_preorder(self):
        print ("ROOT:", self.root.data)
        self._preorder_rec(self.root)

    # ----- Postorder -----
    def _postorder_rec(self, root, level = 1):
        for node in root.child_list:
            self._postorder_rec(node, level + 1)
        print (root.data, end= ", ")

    def print_postorder(self):
        self._postorder_rec(self.root)

    # ----- Count values -----
    def _count_rec(self, root, val):
        for node in root.child_list:
            count = self._count_rec(node, val)
        if root.data == val:
            count += 1
        return 0 + count

    def count(self, val):
        return self._count_rec(self.root, val)

if __name__ == "__main__":
    tree = GeneralTree()
    tree.populate_tree()
    tree.print_preorder()
    tree.print_postorder()
    print ("")
    print (tree.count(5))