def solution(n):
    [x, y] = [1, 0]
    while x + y < n:
        [x, y] = [5 * x + 2 * y + -2, 2 * x + y + -1]
    return x


from time import time


def main():
    start = time()
    print(solution(1000000000000))
    print("elapsed:", time() - start)


main()
