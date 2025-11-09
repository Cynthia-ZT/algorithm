# 给你二叉树的根节点root，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 时间复杂度：O(n)，空间复杂度：O(n)
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ans = []
        cur = [root]
        event = False
        while cur:
            vals = []
            nxt = []
            for node in cur:
                vals.append(node.val)
                if node.left: nxt.append(node.left)
                if node.right: nxt.append(node.right)
            cur = nxt
            # 偶数层翻转
            ans.append(vals[::-1] if even else vals)
            even = not even
        return ans