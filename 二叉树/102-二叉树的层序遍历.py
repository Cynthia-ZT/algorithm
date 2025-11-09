# 给你二叉树的根节点root，返回其节点值的层序遍历。（即逐层地，从左到右访问所有节点）

# 层序遍历，也叫广度优先搜索

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 时间复杂度：O(n)，空间复杂度：O(n)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ans = []
        cur = [root]
        while cur:
            vals = []
            nxt = []
            for node in cur:
                vals.append(node.val)
                if node.left: nxt.append(node.left)
                if node.right: nxt.append(node.right)
            cur = nxt
            ans.append(vals)
        return ans
    
    # 优化空间，用队列(左出右进，先进先出)把cur和nxt合并为一个数组
    # 每层循环的次数，等于进队列前，队列的元素个数
    # 退出循环的条件是队列是否为空
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ans = []
        q = deque([root])
        while q:
            vals = []
            for _ in range(len(q)):
                node = q.popleft()
                vals.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(vals)
        return ans