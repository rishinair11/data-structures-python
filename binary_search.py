from typing import List


def search_in_list(numbers: List, target: int) -> bool:
    start = 0
    end = len(numbers)

    numbers = sorted(numbers)

    while start < end:
        mid = int((start + end) / 2)

        if target == numbers[mid]:
            return True

        if target > numbers[mid]:
            start = mid + 1
            continue
        else:
            end = mid
            continue

    return False
