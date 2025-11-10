# 给定两个整数n和k，返回范围[1,n]中所有可能的k个数的组合。
# 你可以按任何顺序返回答案。

# 设path长为m
# 那么还需要选d=k-m的数
# 设当前需要从[1,i]这i个数中选数
# 如果i < d
# 最后必然无法选出k个数
# 不需要继续递归
# 这是一种剪枝技巧

from typing import List


class Solution:
    # 时间复杂度k*C(n,k)，空间复杂度O(k)
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = [] # [] * k
        def dfs(i):
            d = k - len(path)
            # 或者遍历j的时候写range(i,d-1,-1)
            if i < d:
                return
            if len(path) == k:
                ans.append(''.join(path.copy()))
                return
            for j in range(i, 0, -1):
                path.append(j)
                dfs(j-1)
                path.pop()
        dfs(n)
        return ans