# Definition for singly-linked list.
# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        # if head == None:
        pre_node = head
        cur_node = head

        if cur_node == None:
            return None
        elif cur_node.next == None:
            if cur_node.val == val:
                return None
            else:
                return cur_node

        while cur_node.next != None :
            if cur_node.val == val:
                # remove element
                if cur_node == head:
                    head = cur_node.next
                    cur_node = cur_node.next
                else:

            else:
                cur_node = cur_node.next
