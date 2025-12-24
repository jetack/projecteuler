from datetime import datetime
from time import time

fns = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]


def get_possibilities(lst):
    def recur(lst, rst=set()):
        if len(lst) == 1:
            t = lst[0]
            if t == int(t) and t > 0:
                rst.add(t)
            return 0
        for i in range(len(lst)):
            a = lst.pop(i)
            for j in range(len(lst)):
                b = lst.pop(j)
                for [k, f] in enumerate(fns):
                    if k == 3 and b == 0:
                        continue
                    recur(lst + [f(a, b)])
                lst.insert(j, b)
            lst.insert(i, a)
        return rst

    return sorted(recur(lst))


def count_consecutive(ss):
    for i in range(1, len(ss)):
        if not i in ss:
            return i - 1
    return len(ss)


def get_digits(l=4):
    def recur(path=list(), depth=0, last_i=-1, rst=list()):
        if depth == l:
            rst.append(path)
            return rst
        for i in range(last_i + 1, 10):
            recur(path + [i], depth + 1, i)
        return rst

    return recur()


def solution():
    longest_mem = 0
    wanted_set = None
    for digits in get_digits(4):
        consec = count_consecutive(get_possibilities(digits))
        if consec > longest_mem:
            longest_mem = consec
            wanted_set = digits
    return [longest_mem, wanted_set]


def main():
    start = time()
    print(solution())
    print("elapsed:", time() - start)


if __name__ == "__main__":
    main()

