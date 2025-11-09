# 给定一个二叉树，找到该树中两个指定根节点的最近公共祖先。
# 百度百科中最近公共祖先的定义为：“对于有根树T的两个节点p、q，最近公共祖先表示一个节点x，满足x是p、q的祖先且x的深度尽可能大（一个节点也可以是它自己的祖先）。”

# 分类讨论
# 1. 当前节点是空节点
#       return None也及时当前节点
# 2. 当前节点是p
#       不需要再递归了，因为不论q在p的哪个子树，最近公关祖先都是当前节点了
# 3. 当前节点是q
#       不需要再递归了，因为不论p在q的那个子树，最近公关祖先都是当前节点了
# 4. 当前节点是其他：是否找到p或q
#       (1)左右子树都找到(p和q分别在左右子树)
#           最近公关祖先就是当前节点
#       (2)只有左子树找到(p和q都在左子树)
#           最近公关祖先一定在左子树，返回递归左子树的结果就好
#       (3)只有右子树找到(p和q都在右子树)
#           最近公共祖先一定在右子树，返回递归右子树的结果就好
#       (4)左右子树都没有找到(p和q不在当前节点的左右子树)
#           返回空节点

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 时间复杂度：O(n)，空间复杂度：O(n)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left:
            return left
        return right