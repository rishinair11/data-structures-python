def fetch_nth_fibonacci_number(n: int):
    # starting from 1 and 1
    f_0 = 0
    f_1 = 1
    f_2 = 0

    for i in range(2, n + 1):
        f_2 = f_0 + f_1
        f_0, f_1 = f_1, f_2

    return f_2
