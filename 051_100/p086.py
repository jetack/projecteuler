from math import sqrt


def solution(n):
    m = 0
    rst = 0
    while True:
        m += 1
        for s in range(2, m * 2 + 1):
            if sqrt(s * s + m * m).is_integer():
                rst += s // 2 - max(s - m, 1) + 1
        if rst > n:
            return m


from time import time


def main():
    start = time()
    print(solution(1000000))
    print("elapsed:", time() - start)


main()
