;;; since 9! * 7 = 2540160, n <= 2540160

(defn factorial [n]
  (setv ret 1)
  (while (> n 1)
    (*= ret n)
    (-= n 1))
  ret)

(defn digit-fac-sum [n factorials]
  (setv ret 0)
  (while n
    (+= ret (get factorials (% n 10)))
    (//= n 10))
  ret)

(defn sol [n]
  (setv factorials (lfor i (range 10) (factorial i)))
  (setv ret 0)
  (for [i (range 10 (+ n 1))]
    (if (= i (digit-fac-sum i factorials))
        (+= ret i)))
  ret)

(sol 2540160)
