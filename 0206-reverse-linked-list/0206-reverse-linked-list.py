# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head
        head = None
        while(curr):
            next = curr.next
            if not next:
                head = curr
            curr.next = prev
            prev = curr
            curr = next
        return head