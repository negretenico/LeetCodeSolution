from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    new_nums = sorted(nums)
    ans = []
    for index,num in enumerate(new_nums):
        i, j = index+1, len(new_nums)-1
        if index > 0 and new_nums[index] == new_nums[index-1]:
            continue
        while i<j:
            lower = new_nums[i]
            upper= new_nums[j]
            total = num+lower+upper
            if total==0:
                ans.append([lower,num,upper])
                while (i< j and new_nums[i] == new_nums[i + 1]):
                    i+=1
                while (i< j and new_nums[j] == new_nums[j - 1]):
                    j-=1
                i+=1
                j-=1
            if total > 0:
                j-=1
            if total < 0:
                i+=1
    return ans
