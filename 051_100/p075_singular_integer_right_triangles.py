from math import sqrt


def gcd(m, n):
    return gcd(n, m % n) if m % n else n


def solution(l):
    primitive = set()
    multi_primitive = set()
    rst = 0
    for n in range(1, l):
        for m in range(n + 1, l, 2):
            if gcd(m, n) != 1:
                continue
            t = 2 * m * (m + n)
            if t > l:
                break
            elif t in primitive:
                multi_primitive.add(t)
            else:
                primitive.add(t)
    sieve = [0] * (l + 1)
    for p in primitive:
        for t in range(p, l + 1, p):
            sieve[t] += 1
    for [i, n] in enumerate(sieve):
        if not i in multi_primitive and n == 1:
            rst += 1
    return rst


from time import time


def main():
    start = time()
    print(solution(1500000))
    print("elapsed:", time() - start)


main()
