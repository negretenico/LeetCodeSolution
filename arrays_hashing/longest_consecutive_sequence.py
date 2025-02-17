from typing import List


def longestConsecutive(self, nums: List[int]) -> int:
    maxx= 0
    lookup_set = set(nums)
    for i in lookup_set:
        if (i-1)  in lookup_set:
            continue
        length =1
        while (i+length) in lookup_set:
            length +=1
        maxx = max(length,maxx)
    return maxx
