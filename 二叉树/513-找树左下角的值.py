# 给定一个二叉树的根节点root，请找出该二叉树的最底层最左边节点的值。
# 假设二叉树中至少有一个结点。

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 层序遍历变成从右到左遍历，最后一个就是答案
    # 时间复杂度：O(n)，空间复杂度：O(n)
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque(root)
        while q:
            node =  q.popleft()
            if node.right: q.append(node.right)
            if node.left: q.append(node.left)

        return node.val