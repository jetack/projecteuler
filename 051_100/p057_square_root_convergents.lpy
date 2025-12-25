;;; hy==1.0a4

(defn frac-gen [n]
  (setv numer 3
        denom 2)
  (while n
    (yield [numer denom])
    (-= n 1)
    (setv [numer denom] [(+ numer denom denom) (+ numer denom)])))

(defn sol [n]
  (setv rst 0
        counter 10)
  (for [[numer denom] (frac-gen n)]
    (while (<= counter denom)
      (*= counter 10))
    (if (>= numer counter)
        (+= rst 1)))
  rst)

(sol 1000)
