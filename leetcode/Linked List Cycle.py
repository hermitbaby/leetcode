# Given a linked list, determine if it has a cycle in it.
#
# Follow up:
# Can you solve it without using extra space?



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        """
        1 hashmap or set, save the nodes which has been looked
        2 two pointers, fast and slow

        """

        if head == None or head.next == None:
            return False

        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True

        return False


    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head == None or head.next == None:
            return None

        slow, fast = head, head

        hasCyc = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                hasCyc = True
                break

        if hasCyc:
            slow = head
            while slow != fast:
                slow, fast = slow.next, fast.next
            return slow
        else:
            return None