# 给你一个整数是不足nums, 判断是否存在三元组[nums[i], nums[j], nums[k]]使得i != j, i != k, j != k且nums[i] + nums[j] + nums[k] == 0
# 请你返回所有和为0且不重复的三元组
# 注意：答案中不可以包含重复的三元组

class Solution:
    # 二数之和启发三数之和
    # 时间复杂度：0(n)，空间复杂度：0(1)
    # 因为每个元素最多被遍历一次，所以时间复杂度是线性的
    # 空间复杂度是常数级别的，因为我们只使用了有限的额外空间来存储指针和结果，忽略sorting的空间复杂度的话
    # 一个算法的效率是获取了多少的信息量来衡量一个算法的效率，这个算法通过O(1)的时间获取了O(n)的信息量
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 排序，是用双指针的前提
        nums.sort()
        ans = []
        n = len(nums)
        if nums[0] + nums[1] > target or nums[-1] + nums[-2] < target:
            return ans

        left = 0
        right = n - 1
        while left < right:
            s = nums[left] + nums[right]
            if s < target:
                left += 1
            elif s > target:
                right -= 1
            else:
                ans = ans.append([nums[left], nums[right]])
                # 去重
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
        return ans

    # 遍历每个元素作为三元组的第一个元素，然后在剩下的元素中寻找两个数，使得它们的和等于第一个元素的相反数
    # 时间复杂度：0(n^2)，空间复杂度：0(1)
    # 因为我们对每个元素都调用了一次twoSum函数，而twoSum函数的时间复杂度是线性的
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n-2):
            # 去重, i要大于0才能和前一个元素比较
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            x = nums[i]
            if x + nums[i + 1] + nums[i + 2] > 0:
                break
            if x + nums[-1] + nums[-2] < 0:
                continue

            left = i + 1
            right = n - 1
            while left < right:
                s = x + nums[left] + nums[right]
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    ans.append([x, nums[left], nums[right]])
                    # 去重

                    # 要先让左指针右移，再进行去重判断
                    left += 1
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # 要先让右指针左移，再进行去重判断
                    right -= 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
        return ans
            
