# Reverse a singly linked list.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
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