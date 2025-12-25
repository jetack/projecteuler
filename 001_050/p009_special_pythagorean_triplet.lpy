(defn is-pythagorean? [a b c]
  (= (+ (* a a) (* b b)) (* c c)))

(defn find-triplet [s]
  (for [i (range 1 (- s 1))]
    (for [j (range (+ i 1) (- s 1 i))]
      (setv k (- s i j))
      (if (is-pythagorean? i j k)
            (return (, i j k)))))
  0)

(reduce * (sol 1000))
