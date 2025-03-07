from typing import List


def search(self, nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        middle = l + (r - l) // 2
        guess = nums[middle]

        if guess == target:
            return middle
        if nums[l] <= guess:
            if nums[l] <= target < guess:
                r = middle - 1
                continue
            l = middle + 1
            continue
        if guess < target <= nums[r]:
            l = middle + 1
            continue
        r = middle - 1
    return -1
