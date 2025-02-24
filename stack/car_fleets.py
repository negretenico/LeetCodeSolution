from typing import List


def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    paris = [(p, s) for p, s in zip(position, speed)]
    paris.sort(reverse=True)
    fleets = []
    for p, s in paris:  # Reverse Sorted Order
        fleets.append((target - p) / s)
        if len(fleets) >= 2 and fleets[-1] <= fleets[-2]:
            fleets.pop()
    return len(fleets)
