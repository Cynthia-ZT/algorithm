# 给定一个二叉搜索树，找到该树中两个指定节点的最近公关祖先。

# 分类讨论
# 1. 当前节点是空节点
#   不需要判断，因为题目说p和q一定存在
# 2. p和q都在左子树(p和q都小于当前节点)：返回递归左子树的结果
# 3. p和q都在右子树(p和q都大于当前节点)：返回递归右子树的结果
# 4. 其他：返回当前节点
#   (1)p和q分别在左右子树
#   (2)当前节点是p
#   (3)当前节点是q

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 时间复杂度：O(n)，空间复杂度：O(n)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        x = root.val
        if p.val < x and q.val < x:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > x and q.val > x:
            return self.lowestCommonAncestor(root.right, p, q)
        return root