from typing import List


def reverse_list(list: List) -> List:
    if len(list) == 1:
        return list

    start = 0
    end = len(list) - 1

    while end > start:
        list[end], list[start] = list[start], list[end]
        start += 1
        end -= 1

    return list
