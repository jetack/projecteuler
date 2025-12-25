(defn digit-sum [n]
  (setv rst 0)
  (while n
    (+= rst (% n 10))
    (//= n 10))
  rst)

(defn sol [n]
  (setv rst 0)
  (for [i (range 2 n)]
    (for [j (range 2 n)]
      (setv rst (max rst (digit-sum (** i j))))))
  rst)

(sol 100)

