# Author: Guðjón Ingi Valdimarsson
# Date: 06.02.2020

class Node():
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return str(self.data)
    

def push_front(data, head):
    node = Node(data, head)
    return node

def print_list(head):
    walk = head
    while walk != None:
        print (walk.data)
        walk = walk.next

def print_list_rec(head):
    if head == None:
        return
    else:
        print (head.data)
        return print_list_rec(head.next)

def remove_front(head):
    return head.next

def push_back(data, head):
    walk = head
    while walk.next != None:
        walk = walk.next
    walk.next = Node(data)

def remove_back(head):
    walk = head
    while walk.next.next != None:
        walk = walk.next
    walk.next = None

if __name__ == "__main__":
    head = Node(1)
    print ("Head:", head)
    head = remove_front(head)
    print ("Head:", head)
    for i in range(2, 10):
        head = push_front(i, head)
    push_back(15, head)
    remove_back(head)
    print_list(head)
    #print_list_rec(head)
    #print ("Head:", head)
    #head = remove_front(head)
    #print ("Head:", head)