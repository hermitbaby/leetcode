# Sort a linked list using insertion sort.



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def insertionSortList(self, head):
        if head == None:
            return head

        dummy = ListNode(0)
        dummy.next = head

        # start from 2nd node
        cur = head
        while cur.next:
            if cur.next.val >= cur.val:
                cur = cur.next
            else:
                pre = dummy
                while pre.next.val < cur.next.val:
                    pre = pre.next

                tmp = cur.next
                cur.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp

                #cur.next, pre.next, cur.next.next = cur.next.next, cur.next, pre.next

        return dummy.next