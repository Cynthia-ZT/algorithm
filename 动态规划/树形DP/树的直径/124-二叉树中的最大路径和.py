# 二叉树中的路径被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中至多出现一次。
# 该路径至少包含一个节点，且不一定经过根节点。
# 路径和是路径上各节点值的总和。
# 给你一个二叉树的根节点root，返回其最大路径和。

# 算法
# 遍历二叉树，在计算最大链和的同时，顺带更新答案的最大值。
# 在当前节点[拐弯]的最大路径和 = 左子树的最大链和+右子树的最大链和+当前节点的值
# 返回给父节点的是max(左子树的最大链和，右子树的最大链和)+当前节点值。
# 如果这个值是负数，则返回0，表示不选负数

from cmath import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -inf
        def dfs(node):
            if node is None:
                return 0
            l_sum = dfs(node.left)
            r_sum = dfs(node.right)
            nonlocal ans
            ans = max(ans, l_sum+r_sum+node.val) # type: ignore
            return max(max(l_sum_, r_sum)+node.val, 0) # type: ignore
        dfs(root)
        return ans # type: ignore