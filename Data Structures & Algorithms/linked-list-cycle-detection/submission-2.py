# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        i=1
        if not head or not head.next:
            return False
        slow=head.next
        fast=head.next.next
        while fast!=None and fast.next!=None:
            fast=fast.next.next
            if fast==slow:
                return True
            slow=slow.next
        return False