from bisect import *
from collections import defaultdict
from time import time


def factorize(n, primes):
    res = defaultdict(int)
    k = n
    for p in primes:
        if p > k:
            return res
        while k % p == 0:
            res[p] += 1
            k //= p
    return res


def get_possibilities(factorization):
    factors = []
    for [k, v] in factorization.items():
        factors += [k] * v

    def recur(factors):
        if not factors:
            return [tuple()]
        factor = factors.pop()
        res = set()
        for rep in recur(factors):
            res.add(tuple(sorted(list(rep + (factor,)))))
            for i in range(len(rep)):
                cp = list(rep)
                cp[i] *= factor
                res.add(tuple(sorted(cp)))
        return res

    return recur(factors)


def solution(N=12000):
    primes = [2, 3]
    mem = [None] * (N + 1)
    cnt = N - 1
    n = 3
    while cnt:
        n += 1
        factorization = factorize(n, primes)
        if not factorization:
            primes.append(n)
            continue
        for p in get_possibilities(factorization):
            k = n - sum(p) + len(p)
            if k <= 1 or k > N:
                continue
            if None is mem[k]:
                cnt -= 1
                mem[k] = n
    return sum(set(mem[2:]))


def main():
    start = time()
    print(solution())
    print("elapsed:", time() - start)


if __name__ == "__main__":
    main()

