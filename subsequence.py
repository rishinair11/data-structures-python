def return_short_long_string(string_1: str, string_2: str):
    if len(string_1) < len(string_2):
        return string_1.lower(), string_2.lower()
    else:
        return string_2.lower(), string_1.lower()


def lcs(string_1: str, string_2: str) -> str:
    short, long = return_short_long_string(string_1, string_2)

    if short in long:
        return short

    # create substrings of short
    substr_length = 1
    common_substrings = set()

    while substr_length <= len(short):
        for i in range(len(short) - substr_length + 1):
            if short[i : i + substr_length] in long:
                common_substrings.add(short[i : i + substr_length])

        substr_length += 1

    return max(common_substrings, key=len)
