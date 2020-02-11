# Author: Guðjón Ingi Valdimarsson
# Date: 11.02.2020

class DLL():
    class _Node():
        def __init__(self, data=None, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

        def __str__(self):
            return "{}, {}".format(self.data, self.next).strip(", None, None")

    def _insert_between(self, data, before, after):
        new_node = self._Node(data, after, before)
        before.next = new_node
        after.prev = new_node

    def _remove_node(self, node):
        value = node.data
        node.prev.next = node.next
        node.next.prev = node.prev
        return value

