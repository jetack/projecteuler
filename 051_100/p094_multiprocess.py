from concurrent.futures import ProcessPoolExecutor, as_completed
from math import isqrt


def calc(il, iu):
    rst = 0
    for i in range(il, iu, 2):
        for j in [i - 1, i + 1]:
            l = j // 2
            hsquare = i * i - l * l
            if hsquare == isqrt(hsquare) ** 2:
                rst += i + i + j
    return rst


def solution(limit):
    rst = 0
    max_workers = 16
    ilimit = limit // 3
    i = 3
    [q, r] = divmod(ilimit - i, max_workers)
    gap = q + 1 if r else q
    if gap % 2:
        gap += 1
    boundaries = [i]
    for _ in range(max_workers - 1):
        i += gap
        boundaries.append(i)
    boundaries.append(ilimit)
    bound_pairs = zip(boundaries[:-1], boundaries[1:])
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = (executor.submit(calc, *bound_pair) for bound_pair in bound_pairs)
        for future in as_completed(futures):
            rst += future.result()
    return rst


from time import time


def main():
    start = time()
    print(solution(1000000000))
    print("elapsed:", time() - start)


if __name__ == "__main__":
    main()
