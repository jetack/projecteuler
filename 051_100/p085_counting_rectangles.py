from math import sqrt


def rectangles(m, n):
    return m * (m + 1) * n * (n + 1) // 4


def solve_n(m, r):
    return int(
        (sqrt(m * m * (m + 1) * (m + 1) + 16 * r * m * (m + 1)) - m * (m + 1))
        / (2 * m * (m + 1))
    )


def solution(r):
    nearest = 0
    rst = 0
    for m in range(1, 2001):
        n = solve_n(m, r)
        for j in [n, n + 1]:
            k = rectangles(m, j)
            if abs(k - r) < abs(nearest - r):
                nearest = k
                rst = m * n
    return rst


from time import time


def main():
    start = time()
    print(solution(2000000))
    print("elapsed:", time() - start)


main()
