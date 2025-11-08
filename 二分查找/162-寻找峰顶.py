# 峰值元素是指其值严格大于左右相邻值的元素。
# 给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。
# 你可以假设 nums[-1] = nums[n] = -∞ 。
# 你必须实现时间复杂度为 O(log n) 的算法来解决此问题。

# 虽然存在多个封顶，但是我们可以假设要找的就是其中一个
# 红蓝染色法
# 红色背景表示false，即目标峰顶的左侧
# 蓝色背景表示true，即目标峰顶及其右侧
# 白色表示不确定
# 可以通过比较M和M+1指向的元素大小，来判断目标峰顶的位置
# 如果M位置的元素小于M+1位置的元素，说明目标峰顶在M的右侧
# 如果M位置的元素大于M+1位置的元素，说明目标峰顶在M的位置或者左侧

class Solution:
    # 时间复杂度：0(log n)，空间复杂度：0(1)
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left = -1
        # right指向n-1，因为根据题目n位置的元素一定在峰顶的右侧
        right = n - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid  # (mid, R)
            else:
                right = mid  # (L, mid)
        return right