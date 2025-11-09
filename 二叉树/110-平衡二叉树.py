# 给定一个二叉树，判断它是否是高度平衡的二叉树。
# 本题中，一颗高度平衡的二叉树定义为：
# 一个二叉树每个结点的左右两个子树的高度差的绝对值不超过1.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # 时间复杂度：O(n)，空间复杂度：O(n)
        def depth(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            l_depth = depth(root.left)
            # 在递归中发现不平衡了，应该结束递归直接返回
            if l_depth == -1:
                return -1
            r_depth = depth(root.right)
            if r_depth == -1 or abs(l_depth - r_depth) > 1:
                return -1
            return max(l_depth, r_depth) + 1
        return depth(root) != -1