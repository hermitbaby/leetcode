# Sort a linked list in O(n log n) time using constant space complexity.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def sortList(self, head):
        if head == None or head.next == None:
            return head

        p_slow, p_fast = head, head
        while p_fast.next and p_fast.next.next:
            p_slow = p_slow.next
            p_fast = p_fast.next.next

        head1 = head
        head2 = p_slow.next
        p_slow.next = None

        head1 = self.sortList(head1)
        head2 = self.sortList(head2)

        head = self.merge(head1, head2)
        return head

    def merge(self, head1, head2):
        """
        merge two linkedlist
        """
        if head1 == None:
            return head2
        if head2 == None:
            return head1

        dummy = ListNode(0)
        # pointer_merge
        p1, p2, pm = head1, head2, dummy

        while p1 and p2:
            if p1.val < p2.val:
                pm.next = p1
                p1 = p1.next
            else:
                pm.next = p2
                p2 = p2.next
            pm = pm.next

        if p1 == None:
            pm.next = p2
        if p2 == None:
            pm.next = p1

        return dummy.next


