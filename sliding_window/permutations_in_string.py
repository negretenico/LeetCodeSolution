from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        r = len(s1)
        m = Counter(s1)
        for i in range(0,len(s2)-r+1):
            s_prime = s2[i:i+r]
            if Counter(s_prime) == m:
                return True
        return False
