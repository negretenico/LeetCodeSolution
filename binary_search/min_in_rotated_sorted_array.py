from typing import List


def findMin(self, nums: List[int]) -> int:
    l, r = 0, len(nums) - 1
    while l < r:
        middle = l + (r - l) // 2
        guess = nums[middle]
        if guess > nums[r]:
            l = middle + 1
            continue
        r = middle
    return nums[l]
