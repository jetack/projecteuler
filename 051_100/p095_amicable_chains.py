from collections import Counter


def primes(n):
    rst = [0, 0] + [1] * n
    for [i, pp] in enumerate(rst):
        if pp:
            for j in range(2 * i, n + 1, i):
                rst[j] = 0
    return [i for [i, p] in enumerate(rst) if p]


def factor_sum(factors, f=1):
    if not factors:
        return f
    else:
        [p, n] = factors.pop()
        rst = 0
        this_p = 1
        for i in range(n + 1):
            rst += factor_sum(factors, f * this_p)
            this_p *= p
        factors.append([p, n])
        return rst


def solution(n):
    ps = primes(n)
    met = set()

    def prime_factors(n):
        rst = Counter()
        for p in ps:
            if p > n:
                break
            while n % p == 0:
                rst[p] += 1
                n //= p
        return list(rst.items())

    mem = 0
    rst = 0
    for i in range(2, n + 1):
        if i in met:
            continue
        met.add(i)
        ami_chain = [i]
        t = i
        while (
            (t := (factor_sum(prime_factors(t)) - t)) <= n
            and t != 1
            and (not t in met)
            and (not t in ami_chain)
        ):
            ami_chain.append(t)
            met.add(t)
        if t in ami_chain:
            pos = ami_chain.index(t)
            if len(ami_chain) - pos > mem:
                mem = len(ami_chain) - pos
                rst = min(ami_chain[pos:])
    return rst


from time import time


def main():
    start = time()
    print(solution(1000000))
    print("elapsed:", time() - start)


main()
