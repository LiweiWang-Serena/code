# LeetCode 242. Valid Anagram (Easy)
# Mock OA 2026-10-28: all tests passed
#
# 1. Understand the problem: this mean the length of the string is same and the words count are same no matter how they ranged
# 2. Data structures: dict
# 3. Algorithm: key = a, value = 1 if k,v in s == k,v in t, compare letter counts with Counter
# 4. Time and space complexity: time O(N) space：O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_s = {}
        d_t = {}
        for x in s:
            d_s[x] = d_s.get(x, 0) + 1
        for x in t:
            d_t[x] = d_t.get(x, 0) + 1
        return d_s == d_t
