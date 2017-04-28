#! /usr/bin/env python


class Node:
    def __init__(self):
        self.data = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.cur_node = None

    def add_node(self, data):
        new_node = Node()
        new_node.data = data
        new_node.next = self.cur_node   # always add new node to head
        self.cur_node = new_node        # change current ref of head

    def list_print(self):
        node = self.cur_node
        while node:
            if node.next is None:
                print str(node.data),
            else:
                print str(node.data) + ' -> ',
            node = node.next


ll = LinkedList()
for x in range(10):
    ll.add_node(x)

ll.list_print()