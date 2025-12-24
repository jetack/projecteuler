from functools import cache
from time import time


@cache
def p(n):
    if n < 0:
        return 0
    elif n <= 1:
        return 1
    k = 1
    res = 0
    while (3 * k - 1) * k // 2 <= n:
        lt = n - (3 * k - 1) * k // 2
        rt = n - (3 * k + 1) * k // 2
        tk = (-1) ** (k + 1) * (p(lt) + p(rt))
        res += tk
        k += 1
    return res


def solution():
    n = 1
    while p(n) % 1000000:
        n += 1
    return n


def main():
    start = time()
    print(solution())
    print("elapsed:", time() - start)


if __name__ == "__main__":
    main()

