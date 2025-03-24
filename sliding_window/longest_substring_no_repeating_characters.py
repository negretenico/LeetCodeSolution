class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0
        l, r = 0, 1
        ans = 1
        while r < len(s):
            char = s[r]
            sub = s[l:r]
            if char in sub:
                l += 1
                continue
            r += 1
            ans = max(ans, len(sub) + 1)
        return ans
