# 给你一个二叉树的根节点root，检查他是否轴对称

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 时间复杂度：O(n)，空间复杂度：O(n)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p or q is None:
            return p is q
    
        return p.val == q.val and self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSameTree(root.left, root.right)