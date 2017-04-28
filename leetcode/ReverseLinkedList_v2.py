# -*- coding: utf-8 -*-
from rcviz import callgraph, viz



class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.head = None

    def add_node_to_head(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def print_list(self, head=None):
        cur = self.head if not head else head
        while cur:
            output = str(cur.val) + ' ->' if cur.next else str(cur.val)
            print output,
            cur = cur.next
        print ''

    def init_list(self):
        for x in xrange(4):
            self.add_node_to_head(x)
        self.print_list()

    def reverse_list(self):

        # cur = self.head
        # next = cur.next
        #
        # while cur and next:
        #     if next.next:
        #         tmp = next.next
        #     next.next = cur
        #     cur.next = None
        #     cur = next

        pre = None
        cur = self.head

        while cur:           # 线性循环，只用一个循环变量即可；pre和next在合适的时间，初始化即可；引进pre，极大的简化了next的逻辑
            next = cur.next  # save link
            cur.next = pre   # change direction
            pre = cur        # increase loop var
            cur = next

        self.print_list(pre)
        return pre


    # @viz
    def recursively_reverse_list(self, head):
        if head is None or head.next is None:       # 当head从头，通过递归调用一步步走到，倒数第二个元素时停止
            return head

        tmp = self.recursively_reverse_list(head.next)  # tmp 永远返回原链表末尾的元素，作为head；

        head.next.next = head
        head.next = None
        return tmp






ll = LinkedList()
ll.init_list()
# ll.reverse_list()
# h = ll.recursively_reverse_list(ll.head)
# ll.print_list(h)


def print_list(head=None):
    cur = head
    res = ''
    while cur:
        output = str(cur.val) + ' ->' if cur.next else str(cur.val)
        res += output
        print output,
        cur = cur.next
    print ''
    res += ''
    return res


@viz
def recursively_reverse_list( head):
    if head is None or head.next is None:  # 当head从头，通过递归调用一步步走到，倒数第二个元素时停止
        return head

    tmp = print_list(head)
    recursively_reverse_list.track( tmp=tmp)

    tmp = recursively_reverse_list(head.next)

    head.next.next = head
    head.next = None
    return tmp

h = recursively_reverse_list(ll.head)
ll.print_list(h)
callgraph.render("pic/rr.svg")

