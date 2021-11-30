from data_structures import Queue


def rotate_list(list: list, k: int) -> list:
    q = Queue()

    for item in list:
        q.push(item)

    for i in range(k):
        q._rotate()

    return q._get()
