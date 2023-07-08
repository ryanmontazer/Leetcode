# Time: O(h)
# Space: O(1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (root.val-p.val)*(root.val-q.val)<0:
            return root
        elif root.val==p.val:
            return p
        elif root.val==q.val:
            return q
        elif root.val<p.val:
           return self.lowestCommonAncestor(root.right,p,q)
        else:
            return self.lowestCommonAncestor(root.left,p,q)
