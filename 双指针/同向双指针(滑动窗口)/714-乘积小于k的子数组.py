# 给你一个整数数组nums和一个整数k，请你返回子数组内所有元素乘积小于k的连续子数组的数目。

from typing import List


class Solution:
    # 时间复杂度：0(n)，空间复杂度：0(1)
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
       left = 0
       prod = 1
       ans = 0
       if k <= 1:
            return 0
       for right, x in enumerate(nums):
            prod *= x
            while prod >= k and left <= right:
                prod /= nums[left]
                left += 1

            # 视频里没有判断prod < k
            if prod < k:
                # left, right之间的子数组个数是right - left + 1
                # [l, r], [l+1, r], [l+2, r], ..., [r, r]
                ans += right - left + 1
       return ans