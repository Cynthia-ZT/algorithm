# 给定n个非负整数表示每个宽度为1的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

from typing import List


class Solution:

    # 每个单位能接多少水取决于它左边最高的柱子和右边最高的柱子中较矮的那个
    # 减去当前柱子的高度
    # 时间复杂度：0(n)，空间复杂度：0(n)
    # def trap(self, height: List[int]) -> int:
    #     n = len(height)
    #     pre_max = [0] * n
    #     pre_max[0] = height[0]
    #     for i in range(1, n):
    #         pre_max[i] = max(pre_max[i - 1], height[i])

    #     suf_max = [0] * n
    #     suf_max[n - 1] = height[n - 1]
    #     for i in range(n - 2, -1, -1):
    #         suf_max[i] = max(suf_max[i + 1], height[i])
        
    #     ans = 0
    #     # for i in range(n):
    #     #     ans += min(pre_max[i], suf_max[i]) - height[i]
    #     for h, pre, suf in zip(height, pre_max, suf_max):
    #         ans += min(pre, suf) - h
    #     return ans

    # 双指针优化空间复杂度
    # 时间复杂度：0(n)，空间复杂度：0(1)
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        ans = 0
        pre_max = 0
        suf_max = 0
        # 小于等于是因为左右指针相等的时候，还是可以算当前位置能接的水
        while left <= right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            if pre_max < suf_max:
                ans += pre_max - height[left]
                left += 1
            else:
                ans += suf_max - height[right]
                right -= 1
        return ans