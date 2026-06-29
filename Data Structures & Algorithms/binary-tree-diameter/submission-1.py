# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxdiameter=0
        def countDown(node: Optional[TreeNode])->int:
            nonlocal maxdiameter
            if not node:
                return 0
            leftHeight=countDown(node.left)
            rightHeight=countDown(node.right)
            d=leftHeight+rightHeight
            maxdiameter=max(maxdiameter,d)
            return max(leftHeight,rightHeight)+1
        rootd=countDown(root)
        return maxdiameter