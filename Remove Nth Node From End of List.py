# Given a linked list, remove the nth node from the end of list and return its head.
#
# For example,
#
#    Given linked list: 1->2->3->4->5, and n = 2.
#
#    After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.
# Try to do this in one pass.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        """
        one pointer goes n steps first, then second starts to go
        """
        # if has only one or 0 node, just return empty
        if head == None or head.next == None:
            return None

        p1, p2 = head, head
        # n or n-1
        # because p1 is none, then the gap is n, not n-1
        for i in xrange(n):
            p1 = p1.next
        if p1 == None:
            head = head.next
            return head

        pre = None
        while p1:
            p1 = p1.next
            pre = p2
            p2 = p2.next
        pre.next = p2.next

        return head


    def __init__(self):
        self.cur_node = None


    def initList(self):
        for i in xrange(10):
            self.add_node2head(i)

    def printList(self, head=None):
        if head:
            cur = head
        else:
            cur = self.cur_node

        while cur:
            if cur.next == None:
                print str(cur.val),
            else:
                print str(cur.val) + ' -> ',
                # print str(cur.val) + ' id:' + str(id(cur)) + ' -> ',
            cur = cur.next
        print '\n'

    def add_node2head(self, val):
        new_node = ListNode(val)
        new_node.next = self.cur_node
        self.cur_node = new_node


s = Solution()
s.initList()
s.printList()

head = s.removeNthFromEnd(s.cur_node, 10)
s.printList(head)
