# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dm = ListNode(0, head)
        slow, fast = dm, dm
        for _ in range(n+1):
            fast = fast.next

        while fast != None:
            slow = slow.next
            fast = fast.next

        rm = slow.next
        nxt = rm.next
        slow.next = nxt

        return dm.next