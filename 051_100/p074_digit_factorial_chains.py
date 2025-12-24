# elapsed: 0.7229983806610107
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


digit_factorials = list(map(factorial, range(10)))


def canonicalize(n):
    return int("".join(sorted(list(str(n)), reverse=True)))


def solution(M):
    mem = {}
    rst = 0

    def chain(n):
        lst = []
        rst = 0
        while not n in mem and (not n in lst):
            rst += 1
            lst.append(n)
            n = canonicalize(sum(map(lambda x: digit_factorials[int(x)], str(n))))
        return [lst, n]

    for i in range(M):
        i = canonicalize(i)
        [lst, n] = chain(i)
        if n in mem:
            l = mem[n]
            while lst:
                l += 1
                mem[lst.pop()] = l
        else:
            lst2 = []
            while lst and lst[-1] != n:
                lst2.append(lst.pop())
            l2 = len(lst2)
            l = l2
            while lst:
                l += 1
                mem[lst.pop()] = l
            while lst2:
                mem[lst2.pop()] = l2 + 1
        if mem[i] == 60:
            rst += 1
    return rst


from time import time


def main():
    start = time()
    print(solution(1000000))
    print("elapsed:", time() - start)


main()


# translated from below s-expression

# ;;; from version 0.1.9
# (defmacro fn [*x]
#   (return `(lambda ~@x)))
#
# (def factorial [n]
#   (if (< n 2)
#       (return 1)
#       (return (* n (factorial (- n 1))))))
#
# (= digit-factorials (list (map factorial (range 10))))
#
# (def canonicalize [n]
#   (return (int (.join "" (sorted (list (str n)) :reverse True)))))
#
# (def solution [M]
#   (= mem {})
#   (= rst 0)
#   (def chain [n]
#     (= lst [])
#     (= rst 0)
#     (while (and (not (in n mem))
#                 (not (in n lst)))
#       (+= rst 1)
#       (lst.append n)
#       (= n (canonicalize (sum (map (fn [x] (sub digit-factorials (int x))) (str n))))))
#     (return [lst n]))
#   (for i (range M)
#     (= i (canonicalize i))
#     (= [lst n] (chain i))
#     (if (in n mem)
#         (do (= l (sub mem n))
#             (while lst
#               (+= l 1)
#               (= (sub mem (lst.pop)) l)))
#         (do (= lst2 [])
#             (while (and lst (!= (sub lst -1) n))
#               (lst2.append (lst.pop)))
#             (= l2 (len lst2))
#             (= l l2)
#             (while lst
#               (+= l 1)
#               (= (sub mem (lst.pop)) l))
#             (while lst2
#               (= (sub mem (lst2.pop)) (+ l2 1)))))
#     (if (== (sub mem i) 60)
#         (+= rst 1)))
#   (return rst))
#
# (defmacro euler [*inputs]
#   (return `(do (from time [time])
#
#                (def main []
#                  (= start (time))
#                  (print (solution ~@inputs))
#                  (print "elapsed:" (- (time) start)))
#
#                (main))))
#
# (euler 1000000)
