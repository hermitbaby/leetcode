# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        """
        idea 1: get all values, add them in array, sort them, then generate a new linkedlist
        idea 2: dynamically change the next pointer
        """
        dummy = ListNode(0)
        cur = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                cur, l1 = cur.next, l1.next
            else:
                cur.next = l2
                cur, l2 = cur.next, l2.next

        if l1 == None:
            cur.next = l2
        else:
            cur.next = l1

        return dummy.next



    def __init__(self):
        self.cur_node = None
        self.head = None


    def initList(self):
        for i in ([1, 3, 5, 7]):
            self.add_node2tail(i)


    def initList2(self):
        for i in ([2, 4, 6, 8, 10]):
            self.add_node2tail(i)


    def printList(self, head=None):
        if head:
            cur = head
        else:
            cur = self.head

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


    def add_node2tail(self, val):
        new_node = ListNode(val)
        if self.head == None:
            self.head = new_node
            self.cur_node = new_node
        self.cur_node.next = new_node
        self.cur_node = new_node



s = Solution()
s.initList()
s.printList()

s2 = Solution()
s2.initList2()
s2.printList()

merged_head = s.mergeTwoLists(s.head, s2.head)
s.printList(merged_head)



