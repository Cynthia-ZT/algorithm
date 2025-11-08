# 给定一个含有n个正整数的数组和一个正整数target。
# 找出该数组中满足其和≥target的长度最小的连续子数组[nums]，numsl+1, ..., numsr-1, numsr]，并返回其长度。
# 如果不存在符合条件的子数组，返回0。

class Solution:
    # 时间复杂度：0(n)，空间复杂度：0(1)
    # 因为循环的次数是left+=1的次数(最多是n次)加上right+=1的次数(最多是n次)
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        ans = inf
        s = 0
        for right, x in enumerate(nums):
            s += x
            # 没有判断left <= right，因为当left == right时，s为0，nums[left]根据题目又一定大于0，所以相见会小于0，一定不满足现在的while条件了ß
            # while s - nums[left] >= target:
            #     s -= nums[left]
            #     left += 1
            # if s >= target:
            #     ans = min(ans, right - left + 1)

            # 单调性：左指针移动过程中，while条件一定会从满足变为不满足(也可以从不满足变为满足，见713)
            # 满足单调性才能使用双指针
            while s >= target:
                ans = min(ans, right - left + 1)
                s -= nums[left]
                left += 1
        return ans if ans <= n else 0