# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互联通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会给自动报警。
# 给定一个代表每个房屋存放金额的非负整数数组，计算你不触发警报装置的情况下，一夜之内能够偷窃到的最高金额

# 回溯三问
# 当前操作？枚举第i个房子选或不选
# 子问题？从前i个房子中得到的最大金额和
# 下一个子问题？分类讨论
#   不选：从前i-1个房子中得到的最大金额和
#   选：从前i-2个房子中得到的最大金额和
# dfs(i) = max(dfs(i-1), dfs(i-2)+nums[i])

from functools import cache
from typing import List


class Solution:
    # 时间复杂度在不加cache的时候跟回溯一样，指数级别，加了cache以后，就是记忆化搜索，每中结果只会计算一次，优化到O(n)
    #   计算公式是：状态个数(i的个数，n) * 单个状态计算需要的时间(O(1))
    # 空间复杂度：O(n)
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(i):
            if i < 0:
                return 0
            return max(dfs(i-1), dfs(i-2)+nums[i])
        return dfs(n-1)

        # 把自顶向下(记忆化搜索)
        # 转成自底向上算(递推)
        # dfs -> f数组
        # 递归 -> 递推
        # 递归边界 -> 数组初始值
        # dfs(i) = max(dfs(i-1), dfs(i-2)+nums[i])
        # f[i] = max(f[i-1], f[i-2]+nums[i])
        # 避免负数，都+2：
        # f[i+2] = max(f[i+1], f[i]+nums[i])
        def rob(self, nums: List[int]) -> int:
            n = len(nums)
            f = [0] * (n+2)
            for i, x in enumerate(nums):
                f[i+2] = max(f[i+1], f[i]+x)
            return f[n+1]

        # 优化空间复杂度到O(1)
        # 当前=max(上一个，上上一个+nums[i])
        # f0表示上上一个，f1表示上一个
        # newF = max(f1, f0+nums[i])
        # f0=f1
        # f1=newF
        # 相当于向右整体平移一位
        def rob(self, nums: List[int]) -> int:
            n = len(nums)
            f0=f1=0
            for i, x in enumerate(nums):
                new = max(f1, f0+x)
                f0=f1
                f1=new
            return f1