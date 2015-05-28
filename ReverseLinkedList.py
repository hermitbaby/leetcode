# Reverse a singly linked list.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList0(self, head):
        """
        1 iteratively
        2 recursively
        -- how to check empty list and single node list?
        -- use three pointers to do it?

        SO neat iteration solution
        """
        # dummy = ListNode(0)
        if head == None or head.next == None:
            return head
        pre, cur, next = None, head, head.next
        # while cur and next:
        while cur:
            print cur.val, next.val if next else 'N/A'
            cur.next = pre
            pre, cur, next = cur, next, next.next if next else None
            # pre, cur = cur, next
            # if next == None:
            #     next = None
            # else:
            #     next  = next.next
        return pre


    def reverseList(self, head):
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre


# Reverse a linked list from position m to n. Do it in-place and in one-pass.
#
# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
#
# return 1->4->3->2->5->NULL.
#
# Note:
# Given m, n satisfy the following condition:
# 1 ≤ m ≤ n ≤ length of list.




    def reverseBetween(self, head, m, n):
        """
        !! need more intuitive think on the reverseZone part
        
        1 if m == n, no need to do
        2 need dummy node to find head this time
            the new head will change, according to m,n
            last time, reverse all node, the head must be the last one
            ! this time, head may be changed
        """
        if m == n:
            return head

        if head == None or head.next == None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        # since m starts from 1, not from 0
        for i in xrange(m-1):
            cur = cur.next

        # in my idea, need to save reverseZone head and tail
        #   reverseZone head --> afterReverseZone node
        #   beforeReverseZone node --> reverseZone tail
        reverseZoneHead = cur.next
        for i in xrange(n-m):
            tmp = cur.next
            cur.next = reverseZoneHead.next
            reverseZoneHead.next = reverseZoneHead.next.next
            cur.next.next = tmp
        return dummy.next


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
# s.reverseList(s.cur_node)
node = s.reverseList(s.cur_node)
s.printList(node)