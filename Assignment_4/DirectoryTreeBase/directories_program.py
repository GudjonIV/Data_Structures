# Author: Guðjón Ingi Valdimarsson
# Date: 09.03.2020

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
        while walker.prev != self.head and walker.tree_node < walker.prev.tree_node:
            temp = walker.tree_node
            walker.tree_node = walker.prev.tree_node
            walker.prev.tree_node = temp
            walker = walker.prev
    
    def find_child(self, name):
        walker = self.head.next
        while walker != self.tail:
            if walker.tree_node.name == name:
                return walker
            walker = walker.next
        return False
    
    def rm_child(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def __str__(self):
        ret_str = ""
        walker = self.head.next
        while walker != self.tail:
            ret_str += "\n" + walker.tree_node.name
            walker = walker.next
        return ret_str

class TreeNode():
    def __init__(self, name = ""):
        self.name = name
        self.children = DLL()
    
    def add_subdir(self, name):
        self.children.insert_ordered(TreeNode(name))
    
    def find_dir(self, name):
        return self.children.find_child(name)
    
    def __lt__(self, other):
        return self.name < other.name

    def rm_dir(self, node):
        self.children.rm_child(node)


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
            print("  Listing the contents of current directory,  " + str(tree.name) + str(tree.children))

        elif command[0] == "cd":
            print("  switching to directory " + command[1])
            if command[1] == "..":
                return
            else:
                next_dir = tree.find_dir(command[1])
                if next_dir:
                    run_commands_on_tree(next_dir.tree_node)
                else:    
                    print("  No folder with that name exists")
            print("  current directory: " + str(tree.name))

        elif command[0] == "rm":
            print("  removing directory " + command[1])
            child_dir = tree.find_dir(command[1])
            if child_dir:
                tree.rm_dir(child_dir)
                print("  directory successfully removed!")
            else:
                print("  No folder with that name exists")
        else:
            print("  command not recognized")


def run_directories_program():
    run_commands_on_tree(TreeNode("root"))
    print("Exiting directory program")


if __name__ == "__main__":
    run_directories_program()
    
