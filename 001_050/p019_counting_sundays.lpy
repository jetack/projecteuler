(setv days [0 31 28 31 30 31 30 31 31 30 31 30 31])

(defn leap-year? [y]
  (cond [(= (% y 400) 0) True]
        [(= (% y 100) 0) False]
        [(= (% y 4) 0) True]
        [True False]))

(defn num-days [y m]
  (+ (get days m)
     (if (and (= m 2) (leap-year? y)) 1 0)))

(defn sol [l r]
  (setv ret 0
        cur 0)
  ;; calc first day
  (for [y (range 1900 l)]
    (for [m (range 1 13)]
      (+= cur (num-days y m))))
  (%= cur 7)

  ;; count
  (for [y (range l r)]
    (for [m (range 1 13)]
      (+= ret (if (= cur 6) 1 0))
      (+= cur (num-days y m))
      (%= cur 7)))
  ret)

(sol 1901 2001)
