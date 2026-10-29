# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast = head,head
        ans = None
        flag = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast==slow:
                flag = True
                break
        if not flag:
            return None
        visited = {}
        while head not in visited:
            visited[head] = 1
            head = head.next
        return head