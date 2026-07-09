# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(r1,r2):
            if r1==None or r2==None:
                return r1==r2
            if r1.val==r2.val and sameTree(r1.left,r2.left) and sameTree(r1.right,r2.right):
                return True
            return False

        nq=deque()
        nq.append(root)
        while len(nq)!=0:
            n=nq.popleft()
            if sameTree(n,subRoot):
                return True
            if n.left:
                nq.append(n.left)
            if n.right:
                nq.append(n.right)
        return False