from typing import List


def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    ans= [0] * len(temperatures)
    stack = []
    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] <temp:
            ans[stack[-1]] = i-stack[-1]
            stack.pop()
        stack.append(i)
    return ans
