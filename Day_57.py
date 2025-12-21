# 94. Binary Tree Inorder Traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        elem = []
        if root is None:
            return elem
        if root.left:
            elem += self.inorderTraversal(root.left)
        elem.append(root.val)
        if root.right:
            elem += self.inorderTraversal(root.right)
        return elem

#new approach towards bst learned in leetcode used chatgpt to understand it