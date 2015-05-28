# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# You must do this in-place without altering the nodes' values.
#
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):
        """
        - split list, reverse 2nd list, merge two lists
        - if list length is odd or even
            when split the list, pay attention: when to stop loop
        - how about using double-linked list

        """

        if head == None or head.next == None or head.next.next == None:
            return

        # split list
        slow, fast = head, head
        # if use 'fast and fast.next' will cut the even length list to n+2, n; not n, n
        # why need fast.next??
        #     because if fast.next is none, then fast.next.next will go wrong
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        head1 = head
        head2 = slow.next
        slow.next = None

        # reverse 2nd list
        pre = None
        cur = head2
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        head2 = pre

        # merge two lists
        p1 = head1
        p2 = head2
        # since len(p1) >= len(p2), just check shorter one
        while p2:
            p1_next, p2_next = p1.next, p2.next
            p1.next = p2
            p2.next = p1_next
            p1, p2 = p1_next, p2_next



