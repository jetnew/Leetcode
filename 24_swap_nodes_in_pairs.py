# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        p1 = head
        p2 = head.next
        if p2 == None:
            return p1
        p3 = p2.next
        p1.next = self.swapPairs(p3)
        p2.next = p1
        return p2

