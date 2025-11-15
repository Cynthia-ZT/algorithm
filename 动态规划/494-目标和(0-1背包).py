# 给你一个整数数组nums和一个整数target。
# 向数组中的每个整数前添加‘+’或‘-‘，然后串联起所有证书，可以构造一个表达式：
# 例如，nums = [2, 1]，可以在2之前天街’+‘，在1之前添加’-‘，然后串联起来得到表达式’+2-1‘。
# 返回可以通过上述方法构造的，运算结果等于target的不同表达式数目。

# 思路：相当于从数组中选一些数字取反
# 所有选的正数的和为p
# 所有选的负数的和就是所有数字的和s-p
# 所以target=p-(s-p) => 2p=s+target => p=(s+target)/2
# 所以问题就变成了从nums中选一些数，是他们的和=(s+target)/2
# 并且target不能是负数，s+target得是偶数

# 最后就是0-1背包的变形，0-1背包是至多装capacity，求方案数/最大价值和
# 这道题是恰好装capacity，求方案数/最大/最小价值和
# 还可以有变形至少装capacity, 求求方案数/最小价值和(完全背包的变形)

# 0-1背包的公式：dfs(i) = dfs(i,c) = max(dfs(i-1, c), dfs(i-1, c-w[i])+v[i])
# 因为这题求得是方案数，选和不选都要算上，所以公式从max变成加起来：dfs(i,c) = dfs(i-1, c) + dfs(i-1, c-w[i])

from functools import cache
from typing import List


class Solution:
    # 时间复杂度：O(n*target)因为这里有两个状态，i和c。空间复杂度：O(n*target)
    def findTargetSumWays1(self, nums: List[int], target: int) -> int:
        target += sum(nums)
        if target < 0 or target % 2:
            return 0
        target //= 2

        n = len(nums)
        @cache
        def dfs(i, c):
            if i < 0:
                return 1 if c == 0 else 0
            if c < nums[i]:
                return dfs(i-1, c)
            return dfs(i-1, c) +  dfs(i-1, c-nums[i])
        return dfs(n-1, target)

    # 改成递推
    # f[i+1][c] = f[i][c] + f[i][c-w[i]]
    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        target += sum(nums)
        if target < 0 or target % 2:
            return 0
        target //= 2

        n = len(nums)
        
        f = [[0] * (target+1) for _ in range(n+1)]
        # 根据递归边界，并且递推i还加了1
        f[0][0] = 1
        for i, x in enumerate(nums):
            for c in range(target+1):
                if c < x:
                    f[i+1][c] = f[i][c]
                else:
                    f[i+1][c] = f[i][c] + f[i][c-x]
        return f[n][target]

    # f的结果只跟前一个的结果有关，所以f2的结果可以放到f0里，f3的结果可以放到f1里，所以可以直接把f[i+1]和f[i]模2，降低空间复杂度
    # 空间复杂度O(target)
    def findTargetSumWays3(self, nums: List[int], target: int) -> int:
        target += sum(nums)
        if target < 0 or target % 2:
            return 0
        target //= 2

        n = len(nums)
        
        f = [[0] * (target+1) for _ in range(n+1)]
        # 根据递归边界，并且递推i还加了1
        f[0][0] = 1
        for i, x in enumerate(nums):
            for c in range(target+1):
                if c < x:
                    f[(i+1)%2][c] = f[i%2][c]
                else:
                    f[(i+1)%2][c] = f[i%2][c] + f[i%2][c-x]
        return f[n%2][target]

    # 可以直接简化成一个数组，计算i+1的方案数就是往前数两个的方案数加上i的方案数，倒着算，因为正着算会把往前数两个的数字覆盖掉
    # i:    1 2 3 5 6 7 9
    # i+1:  1 2 3 5 6 7 9
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target += sum(nums)
        if target < 0 or target % 2:
            return 0
        target //= 2

        n = len(nums)
        
        f = [0] * (target+1)
        # 根据递归边界，并且递推i还加了1
        f[0] = 1
        for x in nums:
            for c in range(target+1, x-1, -1):
                # 不需要判断c>=x，因为c的最小范围已经是x-1了
                f[c] = f[c] + f[c-x]
        return f[target]