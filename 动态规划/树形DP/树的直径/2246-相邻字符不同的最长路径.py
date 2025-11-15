# 给你一棵 树（即一个连通、无向、无环图），根节点是节点 0 ，这棵树由编号从 0 到 n - 1 的 n 个节点组成。用下标从 0 开始、长度为 n 的数组 parent 来表示这棵树，
# 其中 parent[i] 是节点 i 的父节点，由于节点 0 是根节点，所以 parent[0] == -1 。
# 另给你一个字符串 s ，长度也是 n ，其中 s[i] 表示分配给节点 i 的字符。
# 请你找出路径上任意一对相邻节点都没有分配到相同字符的 最长路径 ，并返回该路径的长度。

# 求一般树的直径
# 思路1
# 遍历x结点的子树，把最长链的长度都存到一个列表里，排序，去最大两个

# 思路2
# 遍历x节点的子树的同时求最长和次长
# 如何一次遍历找到最长+次长？
#   如果次长在前面，最长在后面，那么遍历到最长的时候就能算出最长+次长
#   如果最长在前面，次长在后面，那么遍历到次长的时候就能算出最长+次长
# 遍历的时候维护最长长度，一定会在遍历到某颗子树时算出最长+次长

from typing import List


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        g = [[] for _ in range(n)]
        # 从1开始是因为，parent里存的是父节点，0节点的父节点不存在
        # g[i]存着第i个节点的邻居
        # 如parent=[-1,0,0,1,1,2]
        # 执行完以后，就是到0的邻居是1,2；1的邻居是3,4；2的邻居是5
        for i in range(1, n):
            g[parent[i]].append(i)

        ans = 0
        # 求最大链长
        def dfs(x):
            nonlocal ans
            x_len=0
            for y in g[x]:
                # y的最大链长加上他跟父节点链接的边
                y_len = dfs(y) + 1 # type: ignore
                if s[x] != s[y]:
                    ans = max(ans, x_len+y_len) # type: ignore
                    x_len = max(x_len, y_len)
            return x_len
        dfs(0)
        # 求得是节点个数，节点个数是边长加一
        return ans + 1
                