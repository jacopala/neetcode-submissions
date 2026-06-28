# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=head
        b=None
        c=None
        while a!=None:
            if b:
                b.next=c
            c=b
            b=a
            a=a.next
        if b:
            b.next=c
        return b