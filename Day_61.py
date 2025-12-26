# 222. Count Complete Tree Nodes

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root: return 0
        if root.left is None and root.right is None:
            return 1
        if root.left is None:
            return self.countNodes(root.right) + 1
        if root.right is None:
            return self.countNodes(root.left) + 1
        else:
            return self.countNodes(root.right) + self.countNodes(root.left) + 1
