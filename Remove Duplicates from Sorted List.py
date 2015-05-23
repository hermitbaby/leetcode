# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        """
        my first idea is to use two pointers: pre, cur, but then seems that one pointer is enough
        because some elements just need to be removed; no need for temp record for link info
        """
        if head == None or head.next == None:
            return head

        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head



    def __init__(self):
        self.cur_node = None


    def initList(self):
        for i in [1, 2, 2, 3, 3, 3, 4, 5]:
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

head = s.deleteDuplicates(s.cur_node)
s.printList(head)