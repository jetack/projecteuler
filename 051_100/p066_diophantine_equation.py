from math import isqrt, floor
from fractions import Fraction


def solve_pell(d):
    sequence = []
    a0 = isqrt(d)
    r = 0
    p = a0
    q = d - a0**2
    while (a := int(Fraction(a0 + p, q))) != 2 * a0:
        sequence.append(a)
        r += 1
        p = a * q - p
        q = Fraction(d - p * p, q)
    sequence.append(a)
    [p1, p2] = [a0, a0 * sequence[0] + 1]
    for i in range(2, r + 1 if r % 2 else 2 * r + 2):
        [p1, p2] = [p2, sequence[(i - 1) % (r + 1)] * p2 + p1]
    return p2


def solution(D):
    rst = 0
    mem = 0
    for n in range(1, isqrt(D) + 1):
        for d in range(1 + n * n, min(D + 1, (n + 1) ** 2)):
            if (x := solve_pell(d)) >= mem:
                mem = x
                rst = d
    return rst


from time import time


def main():
    start = time()
    print(solution(1000))
    print("elapsed:", time() - start)


main()
