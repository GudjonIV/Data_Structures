
import sys

class AlphabetTree:
    class _Node():
        def __init__(self, data):
            self.data = data
            self.childs = []
        
        def add_child(self, node):
            self.childs.append(node)

    def __init__(self):
        self.root = self._Node("")

    # ----- Add word -----
    def _add_word_rec(self, root, word, level = 1):
        if word == word[:level]:
            root.add_child(self._Node(word))
            return
        for child in root.childs:
            if child.data == word[:level]:
                return self._add_word_rec(child, word, level + 1)
        new_node = self._Node(word[:level])
        root.add_child(new_node)
        return self._add_word_rec(new_node, word, level + 1)

    def add_word(self, word):
        self._add_word_rec(self.root, word)
    
    # ----- print preorder -----
    def _preorder_print(self, root, level = 1):
        for node in root.childs[::-1]:
            print (level * "  |" + " --:", node.data)
            self._preorder_print(node, level + 1)

    def print_all(self):
        print ("ROOT:", self.root.data)
        self._preorder_print(self.root)

    # ----- print preorder leaves -----
    def _preorder_leaves(self, root):
        if root.childs == []:
            print (root.data, end=", ")
        for child in root.childs:
            self._preorder_leaves(child)
        return

    def print_leaves(self):
        self._preorder_leaves(self.root)



if __name__ == "__main__":
    file = open(sys.path[0] + "/alphabet_words.txt")
    
    tree = AlphabetTree()
    
    for line in file:
        tree.add_word(line.strip())

    tree.print_all()
    tree.print_leaves()

    file.close()
















































