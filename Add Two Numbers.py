# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        carry = 0
        p1, p2, cur = l1, l2, dummy

        while p1 and p2:
            tmp_val = p1.val + p2.val + carry
            carry = tmp_val / 10
            digit = tmp_val % 10
            cur.next = ListNode(digit)
            p1, p2, cur = p1.next, p2.next, cur.next

        while p1:
            tmp_val = p1.val + carry
            carry = tmp_val / 10
            digit = tmp_val % 10
            cur.next = ListNode(digit)
            p1, cur = p1.next, cur.next

        while p2:
            tmp_val = p2.val + carry
            carry = tmp_val / 10
            digit = tmp_val % 10
            cur.next = ListNode(digit)
            p2, cur = p2.next, cur.next

        if carry:
            cur.next = ListNode(carry)

        return dummy.next