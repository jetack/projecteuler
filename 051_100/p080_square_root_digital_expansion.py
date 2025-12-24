from math import sqrt


def required_sum(x):
    if sqrt(x).is_integer():
        return 0
    left = 1
    while (left + 1) ** 2 <= x:
        left += 1
    top = left
    rst = top
    for i in range(99):
        x -= top * left
        x *= 100
        left += top
        left *= 10
        top = 0
        while (top + 1) * (left + top + 1) <= x:
            top += 1
        left += top
        rst += top
    return rst


def solution(n):
    return sum([required_sum(i) for i in range(1, n + 1)])


from time import time


def main():
    start = time()
    print(solution(100))
    print("elapsed:", time() - start)


main()
