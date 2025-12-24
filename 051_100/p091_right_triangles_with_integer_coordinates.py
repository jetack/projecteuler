from math import sqrt


def distsquare(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2


def solution(M):
    M += 1
    rst = 0
    for x1 in range(0, M):
        for y1 in range(0, M):
            for x2 in range(x1, M):
                for y2 in range(y1 + 1 if x1 == x2 else 0, M):
                    a = distsquare(x1, y1, x2, y2)
                    b = distsquare(0, 0, x1, y1)
                    c = distsquare(0, 0, x2, y2)
                    [a, b, c] = sorted([a, b, c])
                    if a != 0 and a + b == c:
                        rst += 1
    return rst


from time import time


def main():
    start = time()
    print(solution(50))
    print("elapsed:", time() - start)


main()
