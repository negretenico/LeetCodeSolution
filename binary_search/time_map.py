from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        items = self.map.get(key, [])
        res = ""
        l, r = 0, len(items) - 1
        while l <= r:
            middle = l + (r - l) // 2
            key, t = items[middle]
            if t > timestamp:
                r = middle - 1
                continue
            l = middle + 1
            res = key
        return res
