# 给你一个整数数组nums，找出其中最长严格递增子序列的长度。
# 子序列是由数组派生而来的序列，删除(或者不删除)数组中的元素而不改变其余元素的顺序

# 思路1
# 选或不选：为了比大小，需要知道上一个选的数字

# 思路2
# 枚举选哪个：比较当前选的数字和下一个要选的数字
# 启发思路：
# 枚举nums[i]作为LIS的末尾元素，
# 那么需要枚举nums[j]作为LIS的倒数第二个元素，
# 其中j<i且nums[j]<nums[i]
# 
# 回溯三问
# 当前操作？枚举nums[j]
# 子问题？以nums[i]结尾的LIS的长度
# 下一个子问题？以nums[j]结尾的LIS的长度
#
# dfs(i) = max{dfs(j)}+1    j<i 且 nums[j]<nums[i]

from bisect import bisect_left
from functools import cache
from typing import List


class Solution:
    # 时间复杂度O(n^2)，空间复杂度O(n)
    def lengthOfLIS1(self, nums: List[int]) -> int:
        n = len(nums)
        
        @cache
        def dfs(i):
            res = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    res = max(res, dfs(j))
            return res + 1
        ans = 0
        for i in range(n):
            ans = max(ans, dfs(i))
        return ans

    # f[i] = max{f[j]} +1       j<i 且 nums[j]<nums[i]
    def lengthOfLIS2(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    f[i] = max(f[i], f[j])
            f[i] += 1
        return max(f)

# 思路三
# nums的LIS等价于nums与排序去重后的nums的LCS

# 思路四
# 时间复杂度能进一步优化吗？
# 进阶技巧：交换状态与状态值
# f[i]表示末尾元素为nums[i]的LIS的长度
# g[i]表示长度为i+1的IS的末尾元素的最小值
# 算法：在g上用二分查找快速找到第一个>=nums[i]的下标j.
#   如果j不存在，那么nums[i]直接加到g末尾
#   否则修改g[i]为nums[i].
#   注：这个算法按分类的话，算贪心加二分。

    # 时间复杂度O(nlogn)，空间复杂度O(n)
    def lengthOfLIS3(self, nums: List[int]) -> int:
        g = []
        for x in nums:
            j = bisect_left(g,x)
            if j == len(g):
                g.append(x)
            else:
                g[j]=x
        return len(g)

    # 时间复杂度O(nlogn)，空间复杂度O(1)，
    def lengthOfLIS4(self, nums: List[int]) -> int:
        ng = 0
        for x in nums:
            j = bisect_left(nums,x,0,ng)
            if j == ng:
                nums[ng]=(x)
            else:
                nums[j]=x
        return ng

    # 如果题目允许重复元素
    def lengthOfLIS(self, nums: List[int]) -> int:
        ng = 0
        for x in nums:
            j = bisect_left(nums,x,0,ng)
            if j == ng:
                nums[ng]=(x)
            else:
                nums[j]=x
        return ng