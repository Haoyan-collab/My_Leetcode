# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast = head,head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        cur = slow.next
        slow.next = None

        # reverse
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        cur = prev
        
        while cur:
            hnxt = head.next
            cnxt = cur.next
            head.next = cur
            cur.next = hnxt

            cur = cnxt
            head = hnxt

