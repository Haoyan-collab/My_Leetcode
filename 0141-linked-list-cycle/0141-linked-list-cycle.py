# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = head.next
        if not slow:
            return False
        fast = slow.next
        if not fast:
            return False
        while(fast):
            if slow == fast:
                return True
            if not fast.next:
                return False
            else:
                slow = slow.next
                fast = fast.next.next
        return False