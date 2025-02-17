from collections import defaultdict
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    for s in strs:
        groups[''.join(sorted(s))].append(s)
    return list(groups.values())
