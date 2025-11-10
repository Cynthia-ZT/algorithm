# 找出所有相加之和为n的k个数的组合，且满足下列条件：
# ·只使用数字1-9
# ·每个数字最多使用一次
# 返回所有可能的有效组合的列表。该列表不能包含相同的组合两次，组合可以以任何顺序返回。

# 设还需要选d=k-m个数字
# 设还需要选和为t的数字
# (初始为n，每选一个数字j，就把t减小j)
# 剪枝：
# 1. 剩余数字的数目不够i>d
# 2. t < 0
# 3. 剩余数字即使全部选最大的，和也不够t
#   例如i=5，还需要选d=3个数
#   那么如果t>5+4+3，可以直接返回
#   t>i+...+(i-d+1)=((i+i-d+1)*d)/2

from typing import List


class Solution:
    # 时间复杂度k*C(9,k)，空间复杂度O(k)
    def CombinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []
        def dfs(i, t):
            d = k - len(path)
            if t < 0 or t > (i+i-d+1) * d //2:
                return
            if i < d:
                return
            # 这个时候t==0
            if len(path) == k:
                ans.append(''.join(path.copy()))
                return
            for j in range(i, 0, -1):
                path.append(j)
                dfs(j-1, t-j)
                path.pop()
        dfs(9, n)
        return ans