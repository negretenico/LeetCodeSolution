import math
from typing import List


def minEatingSpeed(self, piles: List[int], h: int) -> int:
    l, r = 1, max(piles)

    while l <= r:
        m = (l + r) // 2
        hours_needed = sum(math.ceil(pile / m) for pile in piles)

        if hours_needed <= h:
            r = m - 1
        else:
            l = m + 1

    return l
