(setv n 100)

(defn sol [n]
  (setv ret 0)
  (for [i (range 1 (+ 1 n))]
    (for [j (range (+ i 1) (+ 1 n))]
      (+= ret (* 2 i j))))
  ret)

(sol 100)
