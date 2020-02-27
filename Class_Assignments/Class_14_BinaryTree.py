# Author: Guðjón Ingi Valdimarsson
# Date: 25.02.2020

class BinaryTree():
    class _Node():
        def __init__(self, data=None, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right
    
    def __init__(self):
        self.root = None
        self.size = 0

# ------- Populate tree -------
    def _populate_rec(self, level = 0, root_data = None):
        if not root_data:
            data_input = input()
        else:
            data_input = root_data.data
        if data_input == "":
            return
        level += 1
        self.size += 1
        print (level * "  |" + "--LEFT:", end = " ")
        left = self._populate_rec(level)
        print (level * "  |" + "--RIGHT:", end = " ")
        right = self._populate_rec(level)
        return self._Node(data_input, left, right)

    def populate_tree(self, root = None):
        if root:
            root = self.root
            root = self._populate_rec(root_data = root)
        else:
            print ("ROOT: ", end= " ")
            self.root = self._populate_rec()

# ------- Preored print -------
    def _preorder_rec(self, root, level=1):
        if root.left != None:
            print (level * "  |" + "--LEFT:", root.left.data)
            self._preorder_rec(root.left, level + 1)
        if root.right != None:
            print (level * "  |" + "--RIGHT:", root.right.data)
            self._preorder_rec(root.right, level + 1)

    def print_preorder(self):
        print ("ROOT:", self.root.data)
        self._preorder_rec(self.root)

# ------- Inorder print -------
    def _inorder_rec(self, root):
        if root.left != None:
            self._inorder_rec(root.left)
        print (root.data, end = ", ")
        if root.right != None:
            self._inorder_rec(root.right)

    def print_inorder(self):
        self._inorder_rec(self.root)


# ------- Postorder print -------
    def _postorder_rec(self, root):
        if root.left != None:
            self._postorder_rec(root.left)
        if root.right != None:
            self._postorder_rec(root.right)
        print (root.data, end= ", ")

    def print_postorder(self):
        self._postorder_rec(self.root)



if __name__ == "__main__":
    tree = BinaryTree()
    tree.populate_tree()
    print ("-----Preorder-----")
    tree.print_preorder()
    print ("\n-----Inorder-----")
    tree.print_inorder()
    print ("\n\n-----Postorder-----")
    tree.print_postorder()
    #tree.populate_tree(tree.root)