# Author: Guðjón Ingi Valdimarsson

class TreeNode():
    def __init__(self, name = "", parent = None):
        self.name = name
        self.parent = parent
        self.child_list = []
    
    def populate(self, node):
        self.child_list.append(node)

    def get_child_list(self):
        for child in self.child_list[::-1]:
            print (child.name)
    
    def find_child(self, name):
        for child in self.child_list:
            if child.name == name:
                return child


def run_commands_on_node(node):
    print("  current directory: " + node.name)
    while True:
        user_input = input()
        command = user_input.split()
        if command[0] == "mkdir":
            print("  Making subdirectory " + command[1])
            node.populate(TreeNode(command[1], node))

        elif command[0] == "ls":
            print("  Listing the contents of current directory,  " + node.name)
            node.get_child_list()

        elif command[0] == "cd":
            print("  switching to directory " + command[1])
            if command[1] == "..":
                if node.name == "root":
                    break
                node = node.parent

            else:
                next_node = node.find_child(command[1])
                if next_node:
                    node = next_node
                else:
                    print("  No folder with that name exists")

        else:
            print("  command not recognized")



def run_directories_program():
    # YOU CAN CHANGE THE WHOLE THING IF YOU LIKE!!
    # YOU CAN DESIGN THIS DIFFERENTLY IF IT SUITS YOU
    run_commands_on_node(TreeNode("root"))

if __name__ == "__main__":
    run_directories_program()
    
