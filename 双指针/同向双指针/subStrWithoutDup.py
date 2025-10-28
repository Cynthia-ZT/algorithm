from typing import Counter


class Solution:
    def subStrWithoutDup(self, s:str):
        # 出滑动窗口以外的key point是判断是否有重复字符
        # 查重复的字符可以利用哈希表，记录字符出现的次数
        # 时间复杂度O(n), 空间复杂度O(1)
        ans = 0
        left = 0
        cnt = Counter()
        for right, x in enumerate(s):
            cnt[x] += 1
            while cnt[x] > 1:
                left += 1
                cnt[s[left]] -= 1
            ans = max(ans, right-left+1)
        return ans
