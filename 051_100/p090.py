from time import time


def get_arrangements(pool, max_depth=6):
    def recur(path=list(), last_d=-1, depth=0, ret=list()):
        if depth == max_depth:
            ret.append(list(path))
            return ret
        for d in range(last_d + 1, len(pool)):
            recur(path + [pool[d]], d, depth + 1)
        return ret

    return recur()


def specific_include(elt, arr):
    return elt in arr or (elt == 6 and 9 in arr) or (elt == 9 and 6 in arr)


def can_represent(arr1, arr4):
    for i in range(1, 10):
        [a, b] = divmod(i * i, 10)
        if not (
            specific_include(a, arr4)
            and specific_include(b, arr1)
            or (specific_include(b, arr4) and specific_include(a, arr1))
        ):
            return False
    return True


def solution():
    arrs = get_arrangements(range(10))
    l = len(arrs)
    res = 0
    for i in range(l):
        for j in range(i + 1, l):
            if can_represent(arrs[i], arrs[j]):
                (res := (res + 1))
    return res


def main():
    start = time()
    print(solution())
    print("elapsed:", time() - start)


if __name__ == "__main__":
    main()

