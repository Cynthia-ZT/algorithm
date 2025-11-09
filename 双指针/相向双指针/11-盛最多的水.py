# 给定一个长度为n的整数数组heights。有n条垂线，第i条线的两个端点是(i, 0)和(i, heights[i])。
# 找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。
# 返回容器可以储存的最大水量。
# 说明：你不能倾斜容器。

from typing import List


class Solution:
    # 时间复杂度：0(n)，空间复杂度：0(1)
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        n = len

        left = 0
        right = n - 1
        while left < right:
            w = right - left
            h = min(heights[left], heights[right])
            area = w * h
            ans = max(ans, area)
            # 移动较短的那条线
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return ans
