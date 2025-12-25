(defn count-for-digit [d]
  (setv lower 1
        upper 10
        n d
        cnt 0)
  (while (and (<= lower n) (< n upper))
    (+= cnt 1)
    (*= lower 10)
    (*= upper 10)
    (*= n d))
  cnt)

(defn sol []
  (setv rst 0)
  (for [i (range 1 10)]
    (+= rst (count-for-digit i)))
  rst)

(sol)
