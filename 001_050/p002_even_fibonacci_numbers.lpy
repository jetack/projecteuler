(setv limit (* 4 (** 10 6)))

(setv a 1
      b 2
      ret 0)

(defn next-fib [a b]
  (, b (+ a b)))

(while (< b limit)
  (+= ret b)
  (for [_ (range 3)]
    (setv (, a b) (next-fib a b))))

(print ret)
