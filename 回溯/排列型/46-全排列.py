# 给定一个不含重复数字的数组nums，返回其所有可能的全排列。你可以任意顺序返回答案。

# 数组path记录路径上的数(已选数字)
# 集合s记录剩余未选数字
# 回溯三问
# 当前操作？从s中枚举path[i]要填入的数字x
# 子问题？构造排列>=i的部分，剩余未选数字集合为s
# 下一个子问题？构造排列>=i+1的部分，剩余未选数字集合为s-{x}
# dfs(i,s)
# · dfs(i+1, s-{x1})
# · dfs(i+1, s-{x2})
# ···
from typing import List

class Solution:
    # 时间复杂度O(n*n!)，n!是因为叶子结点是排列的可能性，时间复杂度可以只看叶子结点数，空间复杂度O(n)
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = [] * n
        n = len(nums)
        def dfs(i, s):
            if i == n:
                ans.append(''.join(path.copy()))
                return 
            for x in s:
                path[i] = x
                dfs(i+1, s-{x})
        dfs(0, set(nums))
        return ans

    # 也可以用一个布尔数组onPath记录path中的数字，如果nums[i]在path中，则onPath位真
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = [] * n
        n = len(nums)
        on_path = [False] * n
        def dfs(i):
            if i == n:
                ans.append(''.join(path.copy()))
                return
            for j in range(n):
                if not on_path:
                    path[i] = nums[j]
                    on_path[j] = True
                    dfs(i+1)
                    # 这里要恢复现场是因为这是排列，这次递归完如果不把这个下表恢复成可选的，后面就没法再选这个数字了
                    on_path[j] = False
        dfs(0)
        return ans