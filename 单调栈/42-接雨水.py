# 给定n个非负整数表示每个宽度为1的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

from typing import List


class Solution:
    # 找上一个更大元素，在找的过程中填坑。
    def trap(self, height: List[int]) -> int:
        ans = 0
        st =[]

        for i, h in enumerate(height):
            while st and h >= height[st[-1]]:
                bottom_h = height[st.pop()]
                if len(st) == 0:
                    break
                left = st[-1]
                dh = min(height[left], h) - bottom_h
                ans += dh * (i-left-1)
            st.append(i)
        return ans