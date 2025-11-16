# 给定一个整数数组temperatures，表示每天的温度，返回一个数组answer，其中answer[i]是指对于第i天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用0代替。

from typing import List


class Solution:
    # 时间复杂度O(n)，因为每个元素每次循环只会pop一次
    # 空间复杂度O(n), 栈存储n个元素，严格来算是O(min(n,U)),U=max-min+1
    # 倒序，去掉不可能是下一个更大的数的下标
    def dailyTemperatures1(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        st = []

        for i in range(n-1, -1, 0-1):
            t = temperatures[i]
            if st and t >= temperatures[st[-1]]:
                st.pop()
            if st:
                ans[i] = st[-1] - i
            st.append(i)
        return ans

    # 正序，去掉已经找到下一个更大树的下标
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        st = []

        for i, t in enumerate(temperatures):
            while st and t > temperatures[st[-1]]:
                j = st.pop()
                ans[j] = i - j
            st.append(i)
        return ans