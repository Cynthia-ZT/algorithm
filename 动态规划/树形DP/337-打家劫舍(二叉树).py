# 小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为root。
# 除了root之外，每栋房子有且只有一个父房子与之相连，一番侦查之后，聪明的小偷意识到这个地方的所有房屋的排列类似于一颗二叉树。
# 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
# 给定二叉树的root。返回在不触动警报的情况下，小偷能够偷取的最高金额。

# 选或不选
# 选当前节点：左右儿子都不能选
# 不选当前节点：左右儿子可选可不选
# 
# 提炼状态：
# 选当前节点，以当前节点为根的子树最大点权和
# 不选当前节点，以当前节点韦根的子树最大点权和
#
# 转移方程
# 选=左不选+右不选+当前节点
# 不选=max(左选，左不选)+max(右选，右不选)
# 最终答案=max(根选，根不选)

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0, 0
            l_rob, l_not_rob = dfs(node.left) # type: ignore
            r_rob, r_not_rob = dfs(node.right) # type: ignore
            rob = l_not_rob + r_not_rob + node.val
            non_rob = max(l_rob, l_not_rob) + max(r_rob, r_not_rob)
            return max(rob, non_rob)
        return max(dfs(root)) # type: ignore
    
    # 如果是一般数
    # 选 = 所有儿子不选节点的和+当前节点
    # 不选 = 所有儿子选或不选的最大值加起来