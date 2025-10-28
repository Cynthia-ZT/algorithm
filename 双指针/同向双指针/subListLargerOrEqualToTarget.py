class Solution:
    def subListLargerOrEqualToTarget(self, nums, target) -> int:
        # 滑动窗口
        # 容易错的点，ans的初始化应该是取最大不可能值，而不是0，因为求的是最小值
        # 双指针应用场景：只有在满足单调性才能用：也就是当指针移动过程中，while循环条件能从满足条件逐渐变成不满足条件，或者从不满足条件变成满足条件
        # 时间复杂度O(n), 空间复杂度O(1)
        ans = len(nums) + 1
        sum = 0
        left = 0
        for right, x in enumerate(nums):
            sum += x
            # while sum - nums[left] >= target:
            #     sum -= nums[left]
            #     left += 1
            # if sum >= target:
            #     ans = min(ans, right - left + 1)
            # or below is the same
            while ans >= target:
                ans = min(ans, right - left + 1)
                sum -= nums[left]
                left += 1
        return ans if ans <= len(nums) else 0
