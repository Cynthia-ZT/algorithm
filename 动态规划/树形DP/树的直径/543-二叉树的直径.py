# 给定一颗二叉树，你需要计算它的直径长度。一颗二叉树的直径长度是任意两个节点路径长度中的最大值。这条路径可能穿过也可能不穿过根节点。

# 换个角度看直径
# 首先路径的起点终点一定在叶子上，因为如果不在叶子上，直径还可以继续延伸下去
# 从一个叶子出发向上，在某个节点[拐弯]，向下到达另一个叶子。得到了由两条链拼起来的路径。(也可能只有一条链)

# 算法
# 遍历二叉树，在计算最长链的同时，顺带把直径算出来。
# 在当前节点[拐弯]的直径长度=左子树的最长链+右子树的最长连+2（加2是因为计算链长的时候，没有算当前节点跟子节点链接的部分）
# 返回给父节点的是以当前节点为根的子树的最长链 = max(左子树的最长链，右子树的最长链)+1

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 递归函数求得是链长，在求链长的过程中求出了ans
    # 时间复杂度O(n)，因为每个结点遍历一次
    # 空间复杂度O(n)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node):
            if node in None:
                return -1
            l_len = dfs(node.left)
            r_len = dfs(node.right)
            nonlocal ans
            ans = max(ans, l_len+r_len+2) # type: ignore
            return max(l_len, r_len) + 1
        dfs(root)
        return ans