import heapq
from typing import List, Counter


def topKFrequent(nums: List[int], k: int) -> List[int]:
    c = Counter[nums]
    return [i for i, _ in heapq.nlargest(k, c.items(), key=lambda x: x[1])]
