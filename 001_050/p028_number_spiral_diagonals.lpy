(defn sol [n]
  (setv ret 1
        cur 1)
  (for [i (range 2 n 2)]
    (for [_ (range 4)]
      (+= cur i)
      (+= ret cur)))
  ret)

(sol 1001)
