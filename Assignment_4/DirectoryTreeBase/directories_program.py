# Author: Guðjón Ingi Valdimarsson
# Date: 08.03.2020

class DLL():
    class _Node():
        def __init__(self, tree_node=None, next=None, prev=None):
            self.tree_node = tree_node
            self.next = next
            self.prev = prev

    def __init__(self):
        self.head = self._Node()
        self.tail = self._Node()
        self.tail.prev = self.head
        self.head.next = self.tail

    def append(self, tree_node):
        new_node = self._Node(tree_node, self.tail, self.tail.prev)
        self.tail.prev.next = new_node
        self.tail.prev = new_node

    def insert_ordered(self, tree_node):
        self.append(tree_node)
        walker = self.tail.prev
        while walker != self.head:
            pass
    
    def find_child(self, name):
        walker = self.head
        while walker.next != None:
            if walker.tree_node.name == name:
                return walker
            walker = walker.next
        return False

    def __str__(self):
        ret_str = ""
        walker = self.head.next
        while walker.next != None:
            ret_str += walker.tree_node.name + "\n"
            walker = walker.next
        return ret_str.strip()

class TreeNode():
    def __init__(self, name = ""):
        self.name = name
        self.children = DLL()
    
    def add_subdir(self, name):
        self.children.insert_ordered(TreeNode(name))
    
    def find_dir(self, name):
        return self.children.find_child(name)


def run_commands_on_tree(tree):
    print("  current directory: " + tree.name)
    while True:
        user_input = input()
        command = user_input.split()
        if command[0] == "mkdir":
            print("  Making subdirectory " + command[1])
            if tree.find_dir(command[1]):
                print("  Subdirectory with same name already in directory")
            else:
                tree.add_subdir(command[1])

        elif command[0] == "ls":
            print("  Listing the contents of current directory,  " + str(tree.name))
            print (tree.children)

        elif command[0] == "cd":
            print("  switching to directory " + command[1])
                # command[1] is the name of the subdirectory that should now become the current directory
            if command[1] == "..":
                if False:
                    print("Exiting directory program")
            else:
                next_dir = tree.find_dir(command[1])
                if next_dir:
                    run_commands_on_tree(next_dir)
                else:    
                    print("  No folder with that name exists")
            print("  current directory: " + str(None)) # Add the name of the current directory here

        elif command[0] == "rm":
            print("  removing directory " + command[1])
                # command[1] is the name of the subdirectory that should now become the current directory
            if True:
                print("  directory successfully removed!")
            else:
                print("  No folder with that name exists")
        else:
            print("  command not recognized")


def run_directories_program():
    # YOU CAN CHANGE THE WHOLE THING IF YOU LIKE!!
    # YOU CAN DESIGN THIS DIFFERENTLY IF IT SUITS YOU
    run_commands_on_tree(TreeNode("root"))

if __name__ == "__main__":
    run_directories_program()
    




'''
Note that all the "if False" and "if True" are simply there to
give you the correct success and error message formats.
You can use if sentences or try catch or any other
means of programming you control flow.
You can make an encapsulting class for everything and start with that,
rather than starting with the single TreeNode("root").
Just make sure the input and output of the program is exactly as
specified and fits with the  expected_out.txt when the tester
program is run with the original commands.txt.
Then feel free to make your own, more extensive tests.
'''