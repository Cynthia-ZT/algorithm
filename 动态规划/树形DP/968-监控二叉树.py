# 给定搞一个二叉树，我们在树的节点上安装摄像头。
# 节点上的每个摄像头都可以监视其付对象，自身及其直接子对象。
# 计算监控树的所有节点所需的最小摄像头数量。

# 有几种方法可以监控一个几点。
# 选或不选
# 1. 选，在这个节点安装摄像头           蓝色
# 2. 不选，在它的父节点安装摄像头       黄色
# 3. 不选，在它的左/右儿子安装摄像头     红色
# 分类讨论
# 子树根节点为蓝色时，这颗子树最少需要多少摄像头
# 子树根节点为黄色时，这颗子树最少需要多少摄像头
# 子树根节点为红色时，这颗子树最少需要多少摄像头
#
# 蓝色节点的儿子是哪种颜色都可以 
#   蓝色=min(左蓝，左黄，左红)+min(右蓝，右黄，右红) + 1
# 黄色节点的儿子不能是黄色，（因为黄色节点没有安摄像头，按了就是蓝色了
#   黄色=min(左蓝，左红)+min(右蓝，右红)
# 红色节点的儿子不能是黄色，且至少有一个儿子是蓝色
#   红色=min(左蓝+右红，左红+右蓝，左蓝+右蓝)
#
# 在讨论根节点：
# 二叉树的根节点没有父节点，不可能是黄色，所以
#   最终答案=min(根节点为蓝色，根节点为红色)
# 
# 递归边界：
# 空节点不能装摄像头，蓝色为inf，表示不合法
# 空节点不需要装监控：红色和红色都为0


from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return inf, 0, 0
            l_choose, l_by_fa, l_by_child = dfs(node.left) # type: ignore
            r_choose, r_by_fa, r_by_child = dfs(node.right) # type: ignore
            choose = min(l_choose, l_by_fa, l_by_child) + min(r_choose, r_by_fa, r_by_child) + 1
            by_fa = min(l_choose, l_by_child) + min(r_choose, r_by_fa, r_by_child)
            by_child = min(l_choose + r_by_child, l_by_child + r_choose, l_choose + r_choose)
            return choose, by_fa, by_child
        choose, _, by_child =dfs(root)
        return min(choose, by_child)
        
    # 变形1
    # 在节点x安装摄像头，需要花费cost[x]
    # 求监控所有节点的最小花费
    # 只需要在算当前节点choose的时候加到1，改成对应的花费就好，也就是cost[node]

    # 变形2
    # 如果红色节点有3个儿子呢？有4个儿子呢？
    # 红色节点的儿子不能是黄色，且至少有一个儿子是蓝色
    # 所以需要化简当前节点是红色的公式
    # 直接去每个儿子红蓝最小的公式：min(蓝1，红1)+min(蓝2，红2)+min(蓝3，红3)
    # 跟红色公式比，多了全部都是红色的情况，如min(5,2)+min(7,6)+min(5,1)，也就是两个儿子都不装，所以cost应该加上有一个装的花费
    # 在这种情况就可以把其中一个改成蓝色，把5改成2，多了3；把6改成7，多了1；把1改成5多了4；多以把6改成7更小。
    # 也就是说，我们要改一个蓝色减去红色最小的儿子，如果蓝色减去红色小于等于0就不用改
    #   黄色=min(蓝1，红1)+min(蓝2，红2)+min(蓝3，红3)
    #   红色=黄色+max(0, min(蓝1-红1，蓝2-红2，蓝3-红3))，当min里得出的是负数，说明至少有一个蓝色了，就不用加了
    #   因为红色一定大于黄色：
    #   所以蓝色也可以化简为去掉红色
    #   蓝色=min(蓝1，黄1)+min(蓝2，黄2)+min(蓝3，黄3) + cost[i]