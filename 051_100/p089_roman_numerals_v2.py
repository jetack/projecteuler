rom_priority = [
    ["CM", 900],
    ["M", 1000],
    ["CD", 400],
    ["D", 500],
    ["XC", 90],
    ["C", 100],
    ["XL", 40],
    ["L", 50],
    ["IX", 9],
    ["X", 10],
    ["IV", 4],
    ["V", 5],
    ["I", 1],
]


def read_roman(s):
    rst = 0
    for [c, m] in rom_priority:
        rst += m * s.count(c)
        s = s.replace(c, "")
    return rst


num_priority = [
    ["M", 1000],
    ["CM", 900],
    ["D", 500],
    ["CD", 400],
    ["C", 100],
    ["XC", 90],
    ["L", 50],
    ["XL", 40],
    ["X", 10],
    ["IX", 9],
    ["V", 5],
    ["IV", 4],
    ["I", 1],
]


def minimal_roman(n):
    rst = []
    for [c, m] in num_priority:
        rst += [c] * (n // m)
        n %= m
    return "".join(rst)


def solution(fname):
    with open(fname, "r") as f:
        romans = map(lambda x: x.strip(), f.readlines())
    rst = 0
    for r in romans:
        rst += len(r) - len(minimal_roman(read_roman(r)))
    return rst


from time import time


def main():
    start = time()
    print(solution("./p089_roman.txt"))
    print("elapsed:", time() - start)


main()
