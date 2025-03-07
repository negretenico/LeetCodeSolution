from typing import List


def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    m = [item for sublist in matrix for item in sublist]
    l, r = 0, len(m) - 1
    while l <= r:
        t = l + (r - l) // 2
        guess = m[t]
        if guess == target:
            return True
        elif target < guess:
            r = t - 1
        else:
            l = t + 1
    return False
