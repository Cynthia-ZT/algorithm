# 给你一个二叉树的根节点root，判断其是否是一个有效的二叉搜索树。
# 有效二叉搜索树定义如下：
# 1. 节点的左子树只包含小于当前节点的数。
# 2. 节点的右子树只包含大于当前接地那的数。
# 3. 所偶左子树和右子树自身也是二叉搜索树。

from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 前序遍历：中左右，先判断，在递归
    # 这里直接修改了函数入参，添加了左右边界并给了默认值，保证了不会影响这个函数的调用
    # 时间复杂度：O(n)，空间复杂度：O(n)
    def isValidBST(self, root: Optional[TreeNode], left=-inf, right=inf) -> bool:
        if root is None:
            return True
        x = root.val
        return left < x < right and self.isValidBST(root.left, left, x) and self.isValidBST(root.right, x, right)
    
    # 中序遍历：左中右，大于上一个节点，因为这种情况下，节点值是严格递增的
    # 时间复杂度：O(n)，空间复杂度：O(n)
    pre = -inf
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if not self.isValidBST(root.left):
            return False
        if root.val <= self.pre:
            return False
        self.pre = root.val
        return self.isValidBST(root.right)
    
    # 后序遍历：左右中，先递归，在判断
    # 时间复杂度：O(n)，空间复杂度：O(n)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                # 为了保证x <= l_max or x >= r_min一定不成立
                return inf, -inf
            l_min, l_max = dfs(root.left)
            r_min, r_max = dfs(root.right)
            x = root.val
            if x <= l_max or x >= r_min:
                return -inf, inf
            return min(l_min, x), max(r_max, x)
        return dfs(root)[1] != inf