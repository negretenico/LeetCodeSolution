from typing import List


def maxProfit(prices: List[int]) -> int:
    l, r = 0, 1
    ans = 0
    while r < len(prices):
        cur_profit = prices[r] - prices[l]
        if cur_profit < 0:
            l = r
            r += 1
            continue
        r += 1
        ans = max(ans, cur_profit)
    return ans
