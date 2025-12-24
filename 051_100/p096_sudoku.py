from collections import deque


def find_contradiction(board):
    for i in range(9):
        s = set()
        for j in range(9):
            if isinstance((x := board[i][j]), set):
                continue
            elif x in s:
                return True
            else:
                s.add(x)
    for i in range(9):
        s = set()
        for j in range(9):
            if isinstance((x := board[j][i]), set):
                continue
            elif x in s:
                return True
            else:
                s.add(x)
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            s = set()
            for k in range(3):
                for l in range(3):
                    if isinstance((x := board[i + k][j + l]), set):
                        continue
                    elif x in s:
                        return True
                    else:
                        s.add(x)
    return False


def eliminate_and_further(board, q, remain):
    while q:
        [i, j] = q.popleft()
        n = board[i][j]
        for k in range(9):
            if isinstance((st := board[k][j]), set):
                st.discard(n)
                if len(st) == 1:
                    m = st.pop()
                    board[k][j] = m
                    remain.remove((k, j))
                    q.append([k, j])
        for k in range(9):
            if isinstance((st := board[i][k]), set):
                st.discard(n)
                if len(st) == 1:
                    m = st.pop()
                    board[i][k] = m
                    remain.remove((i, k))
                    q.append([i, k])
        for k in range((subi := (i // 3 * 3)), subi + 3):
            for l in range((subj := (j // 3 * 3)), subj + 3):
                if isinstance((st := board[k][l]), set):
                    st.discard(n)
                    if len(st) == 1:
                        m = st.pop()
                        board[k][l] = m
                        remain.remove((k, l))
                        q.append([k, l])
    if find_contradiction(board):
        return [False, board]
    if remain:
        [i, j] = remain.pop()
        for m in board[i][j]:
            new_board = [
                [{*n} if isinstance(n, set) else n for n in line] for line in board
            ]
            new_board[i][j] = m
            [solvable, returned] = eliminate_and_further(
                new_board, deque([[i, j]]), {x for x in remain}
            )
            if solvable:
                return [True, returned]
    else:
        return [True, board]
    return [False, board]


def sudoku_solver(board):
    q = deque()
    remain = set()
    for i in range(9):
        for j in range(9):
            if (n := board[i][j]) == 0:
                board[i][j] = set(range(1, 10))
                remain.add((i, j))
            else:
                q.append([i, j])
    return eliminate_and_further(board, q, remain)


def parse_line(line):
    return [int(c) for c in line]


def read_boards(filename):
    boards = []
    with open(filename, "r") as f:
        lines = deque(map(lambda x: x.strip(), f.readlines()))
    while lines:
        lines.popleft()
        boards.append([parse_line(lines.popleft()) for _ in range(9)])
    return boards


def solution(filename):
    boards = read_boards(filename)
    rst = 0
    for b in boards:
        [solved, b] = sudoku_solver(b)
        assert solved, b
        [a, b, c, *_] = b[0]
        rst += a * 100 + b * 10 + c
    return rst


from time import time


def main():
    start = time()
    print(solution("./p096_sudoku.txt"))
    print("elapsed:", time() - start)


main()
