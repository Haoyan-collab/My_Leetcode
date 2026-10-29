# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    # def __lt__(self,other):
    #     return self.val < other.val
import heapq as hp
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        q = []
        for i,l in enumerate(lists):
            if l:
                hp.heappush(q,(l.val,i,l))
        dm = ListNode(-1)
        cur = dm
        while q:
            _,idx,node = hp.heappop(q)
            cur.next = node
            cur = cur.next
            if node.next:
                hp.heappush(q,(node.next.val,idx,node.next))
        
        return dm.next