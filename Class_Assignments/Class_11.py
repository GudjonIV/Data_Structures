class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def insert_node(data, head):
    new_node = Node(data, head)
    return new_node

def print_list(head):
    walk = head
    while walk != None:
        print (walk.data)
        walk = walk.next

def count_list(head): # Worse count
    counter = 0
    walk = head
    while walk != None:
        counter += 1
        walk = walk.next
    return counter

def count_list_recur(head): # Better because shorter and more readable code
    if head == None:
        return 0
    return 1 + count_list_recur(head.next)

def insert_sorted_recur(data, head):
    if head.next == None:
        head.next = Node(data)
        return
    if head.data <= data and head.next.data >= data:
        new_node = Node(data, head.next)
        head.next = new_node
        return
    return insert_sorted_recur(data, head.next)

def insert_sorted(data, head=None):
    if head == None:
        return Node(data)
    elif data <= head.data:
        return Node(data, head)
    insert_sorted_recur(data, head)
    return head

def reverse_list(head):
    if head == None:
        return head
    elif head.next == None:
        return head
    node = reverse_list(head.next)
    head.next.next = head
    head.next = None
    return node

def merge_lists(head1, head2):
    if head1 == None:
        return head2
    if head2 == None:
        return head1
    if head1.data <= head2.data:
        head1.next = merge_lists(head1.next, head2)
        return head1
    else:
        head2.next = merge_lists(head1, head2.next)
        return head2

def merge_sort(head):
    if head.next == None or head == None:
        return head
    node = head
    node_half = head
    while node.next != None and node.next.next != None:
        node = node.next.next
        node_half = node_half.next
    head2 = node_half.next
    node_half.next = None
    return merge_lists(merge_sort(head), merge_sort(head2))



if __name__ == "__main__":
    """
    head = Node(1)
    for i in range(2, 10):
        head = insert_node(i, head)

    print_list(head)
    print ("Normal count:", count_list(head))
    print ("Recursive count:", count_list_recur(head))
    head2 = insert_sorted(1)
    head2 = insert_sorted(2, head2)
    head2 = insert_sorted(4, head2)
    head2 = insert_sorted(3, head2)
    head2 = insert_sorted(10, head2)
    head2 = insert_sorted(6, head2)
    head2 = insert_sorted(5, head2)
    head2 = insert_sorted(12, head2)
    print_list(head2)
    head3 = reverse_list(head2)
    print ("Reverse list")
    print_list(head3)
    print ("---------")
    head4 = insert_sorted(7)
    head4 = insert_sorted(11, head4)
    head4 = insert_sorted(20, head4)
    head4 = insert_sorted(4, head4)
    print_list(head4)
    head5 = merge_lists(head2, head4)
    print_list(head5)
    """
    print ("----------")
    head6 = Node(1)
    head6 = insert_node(6, head6)
    head6 = insert_node(3, head6)
    head6 = insert_node(2, head6)
    print_list(head6)
    print ("----------")
    head6 = merge_sort(head6)
    print_list(head6)
