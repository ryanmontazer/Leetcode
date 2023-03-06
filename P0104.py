# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        left_depth,right_depth=0,0
        if root.left:
            left_depth=self.maxDepth(root.left)
        if root.right:
            right_depth=self.maxDepth(root.right)
        return 1+max(left_depth,right_depth)
