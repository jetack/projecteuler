from math import sqrt


def parse_line(line):
    return map(int, line.split(","))


def solution(fname):
    with open(fname, "r") as f:
        lines = zip(*map(parse_line, f.readlines()))
    last_psum = [0] * 80
    for line in lines:
        down = list(map(sum, zip(last_psum, line)))
        right = [*down]
        left = [*down]
        for i in range(79):
            if (rightmove := (right[i] + line[i + 1])) < right[i + 1]:
                right[i + 1] = rightmove
        for i in range(79, 0, -1):
            if (leftmove := (left[i] + line[i - 1])) < left[i - 1]:
                left[i - 1] = leftmove
        last_psum = list(map(min, zip(down, right, left)))
    return min(last_psum)


from time import time


def main():
    start = time()
    print(solution("p082_matrix.txt"))
    print("elapsed:", time() - start)


main()
