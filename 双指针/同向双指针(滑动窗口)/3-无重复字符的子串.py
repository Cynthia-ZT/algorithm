# 给定一个字符串s，请你找出其中不含有重复字符的最长子串的长度。

from typing import Counter


class Solution:
    # 时间复杂度：0(n)，空间复杂度：0(128) = 0(1)，或者O(len(set(s)))，因为字符集是有限的
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        cnt = Counter() # hashmap, key:字符，value:字符出现的次数
        ans = 0
        for right, x in enumerate(s):
            cnt[x] += 1
            if cnt[x] > 1:
                while cnt[x] > 0:
                    cnt[s[left]] -= 1
                    left += 1
            ans = max(ans, right - left + 1)
        return ans