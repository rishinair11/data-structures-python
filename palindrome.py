def is_palindrome(string: str) -> bool:
    if len(string) == 1:
        return True

    start = 0
    end = len(string) - 1

    while end > start:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1

    return True
