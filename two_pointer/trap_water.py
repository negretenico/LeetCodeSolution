from typing import List


def trap(height: List[int]) -> int:
    i,j = 0, len(height) - 1
    left_max, right_max = height[i], height[j]
    res = 0
    while i<j:
        if left_max < right_max:
            i += 1
            left_max = max(left_max, height[i])
            res += left_max - height[i]
            continue
        j -= 1
        right_max = max(right_max, height[j])
        res += right_max - height[j]
    return res
