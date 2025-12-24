from functools import reduce


def cc_next(pos):
    return [[pos, 14 / 16], [0, 1 / 16], [10, 1 / 16]]


def ch_next(pos):
    nr = 15 if pos == 7 else 25 if pos == 22 else 5
    nu = 12 if pos == 7 else 28 if pos == 22 else 12
    return [
        [pos, 6 / 16],
        [0, 1 / 16],
        [10, 1 / 16],
        [11, 1 / 16],
        [24, 1 / 16],
        [39, 1 / 16],
        [5, 1 / 16],
        [nr, 2 / 16],
        [nu, 1 / 16],
        [pos - 3, 1 / 16],
    ]


def solution(n):
    board = [1] + [0] * 39
    after_jail = [0] * 40
    after_two_jail = [0] * 40
    ccs = {2, 17, 33}
    chs = {7, 22, 36}
    while True:
        newboard = [0] * 40
        new_after_jail = [0] * 40
        new_after_two_jail = [0] * 40
        for [i, ip] in enumerate(board):
            for d1 in range(1, n + 1):
                for d2 in range(1, n + 1):
                    sp = 1 / n / n
                    pos = (i + d1 + d2) % 40
                    if d1 == d2:
                        pspeed = (
                            (n - 1)
                            / n
                            / n
                            / n
                            * (1 - (after_jail[i] + after_two_jail[i]) / ip)
                            + 1 / n / n * (after_two_jail[i] / ip)
                            if ip and i != 10 and (d1 == d2)
                            else 0
                        )
                        newboard[10] += ip * sp * pspeed
                        sp *= 1 - pspeed
                    next_pos = (
                        [[10, 1]]
                        if pos == 30
                        else cc_next(pos)
                        if pos in ccs
                        else ch_next(pos)
                        if pos in chs
                        else [[pos, 1]]
                    )
                    for [pos, pp] in next_pos:
                        newboard[pos] += ip * sp * pp
                        if pos != 10 and i == 10:
                            new_after_jail[pos] += ip * sp * pp
                        if pos != 10 and after_jail[i]:
                            new_after_two_jail[pos] += after_jail[i] * sp * pp
        if board == newboard:
            break
        else:
            board = newboard
            after_jail = new_after_jail
            after_two_jail = new_after_two_jail
    return sorted(enumerate(board), key=lambda x: x[1], reverse=True)[:3]


from time import time


def main():
    start = time()
    print(solution(4))
    print("elapsed:", time() - start)


main()

