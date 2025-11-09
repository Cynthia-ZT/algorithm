# 给定一个二叉树，找出其最大深度。
# 二叉树的深度为根节点到最远叶子结点的最长路径上的节点数。
# 说明：叶子结点是指没有子节点的节点

# 不要一开始就陷入细节
# 而是思考整棵树与其左右子树的关系
# 整棵树的最大深度=max(左子树的最大深度，右子树的最大深度)

# 原问题：计算整棵树的最大深度
# 子问题：计算左/右子树的最大深度
# 子问题与原问题是相似的
# 类比循环，执行的代码也应该是相同的
# 但子问题需要把计算结果返给上一级问题
# 这更适合用递归实现
# 由于子问题的规模比原问题小，不断递下去，总会有尽头
# 即递归的边界条件(base case)，直接返回它的答案(归)

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 时间复杂度：O(n)，因为每个几点都遍历了一次
    # 空间复杂度：O(n)，因为要用一个先进后出的栈结构保存每次的还没有结果的子问题，最差情况需要n个子问题
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth_left = self.maxDepth(root.left)
        depth_right = self.maxDepth(root.right)
        # + 1 是因为要加上root的深度
        return max(depth_left, depth_right) + 1

    # 做法2：
    # 定义递归函数接受节点和当前的节点个数
    # 每次递归更新最大深度ans的值
    # 时间复杂度：O(n)，因为每个几点都遍历了一次
    # 空间复杂度：O(n)，因为要用一个先进后出的栈结构保存每次的还没有结果的子问题，最差情况需要n个子问题
    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root, cnt):
            if root is None:
                return
            cnt += 1
            # python中要更新全局变量，要加一个nonlocal
            nonlocal ans
            ans = max(ans, cnt)
            dfs(root.left, cnt)
            dfs(root.right, cnt)
        dfs(root, 0)
        return ans