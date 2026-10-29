# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        dm_less = ListNode(-1)
        dm_ge = ListNode(-1)
        lidx = dm_less
        gidx = dm_ge
        while head:
            if head.val<x:
                lidx.next = head
                lidx = lidx.next
            else:
                gidx.next = head
                gidx = gidx.next
            head = head.next
        gidx.next = None
        lidx.next = dm_ge.next
        return dm_less.next
