from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
        pairs = {}
        for (i, number) in enumerate(nums):
            compliment = pairs.get(target-number)
            if(compliment is not None):
                return [compliment,i]
            pairs[number] = i
        return []
