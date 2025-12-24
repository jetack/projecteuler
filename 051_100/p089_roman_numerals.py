def read_roman(s):
    i = 0
    rst = 0
    while s[i : i + 1] == "M":
        rst += 1000
        i += 1
    if s[i : i + 2] == "CM":
        rst += 900
        i += 2
    if s[i : i + 1] == "D":
        rst += 500
        i += 1
    if s[i : i + 2] == "CD":
        rst += 400
        i += 2
    while s[i : i + 1] == "C":
        rst += 100
        i += 1
    if s[i : i + 2] == "XC":
        rst += 90
        i += 2
    if s[i : i + 1] == "L":
        rst += 50
        i += 1
    if s[i : i + 2] == "XL":
        rst += 40
        i += 2
    while s[i : i + 1] == "X":
        rst += 10
        i += 1
    if s[i : i + 2] == "IX":
        rst += 9
        i += 2
    if s[i : i + 1] == "V":
        rst += 5
        i += 1
    if s[i : i + 2] == "IV":
        rst += 4
        i += 2
    while s[i : i + 1] == "I":
        rst += 1
        i += 1
    return rst


def minimal_roman(n):
    rst = []
    while n:
        if m := (n // 1000):
            rst += ["M"] * m
            n %= 1000
        elif (c := (n // 100)) == 9:
            rst.append("CM")
            n %= 100
        elif c >= 5:
            rst.append("D")
            n -= 500
        elif c >= 4:
            rst.append("CD")
            n -= 400
        elif c:
            rst += ["C"] * c
            n %= 100
        elif (x := (n // 10)) == 9:
            rst.append("XC")
            n %= 10
        elif x >= 5:
            rst.append("L")
            n -= 50
        elif x >= 4:
            rst.append("XL")
            n -= 40
        elif x:
            rst += ["X"] * x
            n %= 10
        elif n == 9:
            rst.append("IX")
            n = 0
        elif n >= 5:
            rst.append("V")
            n -= 5
        elif n >= 4:
            rst.append("IV")
            n -= 4
        else:
            rst += ["I"] * n
            n = 0
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
