from math import isqrt


def solution(limit):
    rst = 0
    for i in range(3, 1 + limit // 3, 2):
        for j in [i - 1, i + 1]:
            l = j // 2
            hsquare = i * i - l * l
            if hsquare == isqrt(hsquare) ** 2:
                rst += i + i + j
    return rst


from time import time


def main():
    start = time()
    print(solution(1000000000))
    print("elapsed:", time() - start)


main()
