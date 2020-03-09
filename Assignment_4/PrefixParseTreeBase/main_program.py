# Author: Guðjón Ingi Valdimarsson
# Date: 09.03.2020

import sys
from enum import Enum

class DivisionByZero(Exception):
    pass

class UnknownInTree(Exception):
    pass

class OutputFormat(Enum):
    PREFIX = 0
    INFIX = 1
    POSTFIX = 2

class PrefixParseTree:
    class _Node():
        def __init__(self, value, parent=None, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right
            self.parent = parent
        
        def __str__(self):
            return str(self.value)

    def __init__(self):
        self.format = OutputFormat.PREFIX
        self.root = None


# -------- Create tree --------
    def _load_rec(self, statement_list, root, parent=None):
        root = self._Node(statement_list.pop(), parent)
        if root.value in "+-*/":
            root.left = self._load_rec(statement_list, root.left, root)
            root.right = self._load_rec(statement_list, root.right, root)
        return root

    def load_statement_string(self, statement):
        self.root = self._load_rec(statement.split()[::-1], self.root)


# -------- Calculate root --------
    def _calculate(self, val1, val2, opperand):
        if opperand == "+":
            return val1 + val2
        elif opperand == "-":
            return val1 - val2
        elif opperand == "*":
            return val1 * val2
        elif opperand == "/":
            try:
                return val1 / val2
            except ZeroDivisionError:
                raise DivisionByZero()

    def _root_rec(self, root):
        if root.value in "+-/*":
            ret_int1 = self._root_rec(root.left)
            ret_int2 = self._root_rec(root.right)
            return self._calculate(ret_int1, ret_int2, root.value)

        elif root.value.isnumeric():
            return int(root.value)
        
        else:
            raise UnknownInTree()

    def root_value(self):
        return self._root_rec(self.root)


# -------- Simplify --------
    def _simplify_rec(self, root):
        try:
            return self._Node(self._root_rec(root), root.parent)
        except (DivisionByZero, UnknownInTree):
            if root.left != None:
                root.left = self._simplify_rec(root.left)
            if root.right != None:
                root.right = self._simplify_rec(root.right)
        return root

    def simplify_tree(self):
        self.root = self._simplify_rec(self.root)


# -------- Solve unknown --------
    def _solve_inverse(self, val1, val2, opperand, leftBool = True):
        if opperand == "+":
            return val1 - val2

        elif opperand == "-":
            if leftBool:    # If left value is the known one returns the right value
                return val2 - val1
            return val1 + val2  # Else returns the left value

        elif opperand == "/":
            if leftBool:    # If left value is the known one returns the right value
                return val2 / val1
            return val1 * val2  # Else returns the right value

        elif opperand == "*":
            try:
                val1 / val2
            except ZeroDivisionError:
                raise DivisionByZero()

    def _solve_rec(self, value, root):
        if not root.left.value.isnumeric() and root.left.value not in "+-*/": # Check if constant in left node
            return self._solve_inverse(value, self._root_rec(root.right), root.value, False)

        elif not root.right.value.isnumeric() and root.right.value not in "+-*/": # Check if constant in right node
            return self._solve_inverse(value, self._root_rec(root.left), root.value)

        try:    # Try to solve right sub tree
            value1 = self._root_rec(root.right)
            next_val = self._solve_inverse(value, value1, root.value, False)
            return self._solve_rec(next_val, root.left)

        except UnknownInTree:   # Else solve left sub tree
            value1 = self._root_rec(root.left)
            next_val = self._solve_inverse(value, value1, root.value)
            return self._solve_rec(next_val, root.right)
    
    def solve_tree(self, root_value):
        return self._solve_rec(root_value, self.root)


# -------- String functions --------
    def set_format(self, out_format = OutputFormat.PREFIX):
        self.format = out_format 

    def _prefix(self, root):
        ret_str = str(root.value)
        if root.left != None:
            ret_str += " " + self._prefix(root.left)
        if root.right !=  None:
            ret_str += " " + self._prefix(root.right)
        return ret_str

    def _infix(self, root):
        ret_str = ""
        if root.left != None:
            ret_str += "(" + self._infix(root.left) + " "
        ret_str += str(root.value)
        if root.right != None:
            ret_str += " " + self._infix(root.right) + ")"
        return ret_str

    def _postfix(self, root):
        ret_str = ""
        if root.left != None:
            ret_str += self._postfix(root.left) + " "
        if root.right != None:
            ret_str += self._postfix(root.right) + " "
        return ret_str + str(root.value) 

    def __str__(self):
        if self.format == OutputFormat.POSTFIX: 
            return self._postfix(self.root)
        elif self.format == OutputFormat.INFIX:
            return self._infix(self.root)
        else:
            return self._prefix(self.root)


# -------- TESTS --------
def test_prefix_parser(str_statement, solve = False, root_value = 0):

    if solve == True:
        prefix_tree = PrefixParseTree()
        prefix_tree.load_statement_string(str_statement)
        print("PREFIX: " + str(prefix_tree))
        print("The value of x if the root_value is " + str(root_value) + " is: " + str(prefix_tree.solve_tree(root_value)))
    else:
        prefix_tree = PrefixParseTree()
        prefix_tree.load_statement_string(str_statement)
        print("PREFIX: " + str(prefix_tree))
        prefix_tree.set_format(OutputFormat.INFIX)
        print("INFIX: " + str(prefix_tree))
        prefix_tree.set_format(OutputFormat.POSTFIX)
        print("POSTFIX: " + str(prefix_tree))

        str_print = "The value of the tree is: "
        try:
            str_print += str(prefix_tree.root_value())
        except DivisionByZero:
            str_print += str("A division by zero occurred")
        except UnknownInTree:
            str_print += str("There is an unknown value in the tree")
        print(str_print)

        print("SIMPLIFIED:")
        prefix_tree.simplify_tree()
        prefix_tree.set_format(OutputFormat.PREFIX)
        print("PREFIX: " + str(prefix_tree))
        prefix_tree.set_format(OutputFormat.INFIX)
        print("INFIX: " + str(prefix_tree))
        prefix_tree.set_format(OutputFormat.POSTFIX)
        print("POSTFIX: " + str(prefix_tree))

    print("\n\n")

if __name__ == "__main__":
    org_out = sys.stdout
    fout = open(sys.path[0] + "/parse_out.txt", "w+")
    sys.stdout = fout
    f = open(sys.path[0] + "/prefix_statements.txt", "r")
    previous_line = None
    for line in f:
        some_split = line.split()
        if some_split[0] == "solve":
            test_prefix_parser(previous_line.strip(), True, int(some_split[1]))
        test_prefix_parser(line.strip())
        previous_line = line
    f.close()
    sys.stdout = org_out
    fout.close()