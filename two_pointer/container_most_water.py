from typing import List


def maxArea(height: List[int]) -> int:
    ans = float('-infinity')
    i, j = 0, len(height)-1
    while i < j:
        height_to_use = min(height[j],height[i])
        cur_area = height_to_use * (j-i)
        ans= max(ans,cur_area)
        if height[j] > height[i]:
            i+=1
        else:
            j-=1
    return ans
