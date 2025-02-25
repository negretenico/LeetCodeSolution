from typing import List


def search(self, nums: List[int], target: int) -> int:
    l,r =0, len(nums)-1
    while l<=r:
        m = l+(r-l)//2
        x = nums[m]
        if x< target:
            l=m+1
        elif x> target:
            r=m-1
        else:
            return m
    return -1
