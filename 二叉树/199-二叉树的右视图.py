# 给定一个二叉树的根节点root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

# 两个问题，如何记录答案，以及什么时候记录或者更新答案
# 思路：因为要右视图，先递归右子树。当答案的长度等于递归深度时，记录答案

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 时间复杂度：O(n)，空间复杂度：O(n)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(self, node: Optional[TreeNode], depth):
            if node is None:
                return
            if depth == len(ans):
                ans.append(node.val)
            dfs(node.right, depth+1)
            dfs(node.left, depth+1)
        dfs(root, 0)
        return ans

