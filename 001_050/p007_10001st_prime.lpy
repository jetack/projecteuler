(setv n 10001)

(defn is-prime? [n]
  (if (not (% n 2))
      (return False))
  (setv f 3)
  (while (<= (* f f) n)
    (if (not (% n f))
        (return False))
    (+= f 2))
  True)

(defn n-th-prime [n]
  (if (= n 1)
      (return 2))
  (setv cnt 1
        i 3)
  (while (< cnt n)
    (if (is-prime? i)
        (+= cnt 1))
    (+= i 2))
  (- i 2))


(n-th-prime n)
