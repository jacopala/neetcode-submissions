# Definition for a binary tree select.
# class Treeselect:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[Treenode]) -> Optional[Treenode]:
        if not root:
            return None
        
        stack = [root]
        while stack:
            select = stack.pop()
            select.left, select.right = select.right,select.left
            if select.left:
                stack.append(select.left)
            if select.right:
                stack.append(select.right)
        return root