from functools import reduce
from random import randint


def cc_next(pos):
    c = randint(0, 15)
    return pos if c < 14 else 0 if c == 14 else 10


def ch_next(pos):
    c = randint(0, 15)
    nr = 15 if pos == 7 else 25 if pos == 22 else 5
    nu = 12 if pos == 7 else 28 if pos == 22 else 12
    return (
        pos
        if c < 6
        else 0
        if c == 6
        else 10
        if c == 7
        else 11
        if c == 8
        else 24
        if c == 9
        else 39
        if c == 10
        else 5
        if c == 11
        else nr
        if c < 14
        else nu
        if c == 14
        else pos - 3
    )


def solution(n, steps):
    board = [1] + [0] * 39
    ccs = {2, 17, 33}
    chs = {7, 22, 36}
    pos = 0
    consec = 0
    for _ in range(steps):
        d1 = randint(1, n)
        d2 = randint(1, n)
        if d1 == d2:
            consec += 1
        else:
            consec = 0
        if consec == 3:
            pos = 10
        else:
            pos = (pos + d1 + d2) % 40
            if pos == 30:
                pos = 10
            elif pos in ccs:
                pos = cc_next(pos)
            elif pos in chs:
                pos = ch_next(pos)
        if pos == 10:
            consec = 0
        board[pos] += 1
    s = sum(board)
    board = map(lambda x: x / s, board)
    return sorted(enumerate(board), key=lambda x: x[1], reverse=True)[:3]


from time import time


def main():
    start = time()
    print(solution(4, 10000000))
    print("elapsed:", time() - start)


main()
