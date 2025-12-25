(defn sum-of-proper-divisors [n]
  (setv mem (* [1] n)
        (get mem 0) -1)
  (for [i (range 2 n)]
    (for [j (range (* 2 i) n i)]
      (+= (get mem j) i)))
  mem)

(defn calc-abundants [n]
  (lfor (, i s) (enumerate (sum-of-proper-divisors n)) :if (> s i) i))

(defn abun-summable? [i abundants abun-set]
  (for [a abundants]
    (cond [(> a (// i 2)) (break)]
          [(in (- i a) abun-set) (return True)]))
  False)

(defn non-abun-sums [n]
    (setv abundants (calc-abundants n)
        abun-set (set abundants)
        ret [])
  
  (for [i (range 1 n)]
    (if (not (abun-summable? i abundants abun-set))
        (ret.append i)))
  ret)

(defn sol [n]
  (sum (non-abun-sums n)))

(sol 28123)
