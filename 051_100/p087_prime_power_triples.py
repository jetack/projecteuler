from math import sqrt


def get_primes(n):
    rst = [0, 0] + [1] * int(sqrt(n))
    for i in range(2, len(rst)):
        if rst[i]:
            for j in range(2 * i, len(rst), i):
                rst[j] = 0
    return [p for [p, c] in enumerate(rst) if c]


def solution(n):
    primes = get_primes(n)
    squares = list(map(lambda x: x * x, primes))
    cubes = list(map(lambda x: x * x * x, primes))
    quads = list(map(lambda x: x * x * x * x, primes))
    rst = set()
    for s in squares:
        for c in cubes:
            for q in quads:
                if (t := (s + c + q)) > n:
                    break
                rst.add(t)
    return len(rst)


from time import time


def main():
    start = time()
    print(solution(50000000))
    print("elapsed:", time() - start)


main()
