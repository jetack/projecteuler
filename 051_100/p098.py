import lispy

import json
from collections import Counter, defaultdict
from math import isqrt
from time import time


def counter_to_str(d):
    return ",".join(map(lambda x: x[0] + str(x[1]), sorted(d.items())))


def get_all_anagrams(lst):
    mem = defaultdict(list)
    for word in lst:
        mem[counter_to_str(Counter(word))].append(word)
    rst = []
    for [k, v] in mem.items():
        if len(v) >= 2:
            rst.append(v)
    return rst


def square_p(n):
    return n == isqrt(n) ** 2


def find_square_pairs(anagrams):
    candidates = {}
    for d in anagrams[0]:
        candidates[d] = set(range(10))
    for anagram in anagrams:
        candidates[anagram[0]].discard(0)

    def recur(candidates, translation={}, rst=list()):
        if not candidates:
            nums = list(
                filter(
                    square_p,
                    map(
                        lambda x: int("".join(x)),
                        map(
                            lambda w: map(lambda c: str(translation[c]), list(w)),
                            anagrams,
                        ),
                    ),
                )
            )
            if len(nums) >= 2:
                rst.append(nums)
            return rst
        [c, ds] = candidates.popitem()
        for d in ds:
            if not d in translation.values():
                recur(candidates, translation | {c: d})
        candidates[c] = ds
        return rst

    return recur(candidates)


def solution():
    with open("./p098_words.txt", "r") as f:
        s = f.read()
    word_list = json.loads("[" + s + "]")
    res = 0
    for anagrams in get_all_anagrams(word_list):
        square_pairs = find_square_pairs(anagrams)
        if square_pairs:
            res = max(res, max(map(max, square_pairs)))
    return res


def main():
    start = time()
    print(solution())
    print("elapsed:", time() - start)


if __name__ == "__main__":
    main()

