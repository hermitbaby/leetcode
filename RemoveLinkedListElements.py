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
    def removeElements00(self, head, val):
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
                    pass
            else:
                cur_node = cur_node.next

    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, head

        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return dummy.next


    def __init__(self):
        self.cur_node = None


    def initList(self):
        for i in [1,2,3,1,2,3]:
            self.add_node2head(i)

    def printList(self):
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
s.removeElements(s.cur_node, 1)
s.printList()
# s.removeElements()
