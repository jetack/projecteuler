(defn sol [n]
  (setv mem [1]
        rst 0)
  (for [i (range n)]
    (for [j (range (- (len mem) 1) 0 -1)]
      (+= (get mem j) (get mem (- j 1)))
      (if (> (get mem j) 1000000)
          (+= rst 1)))
    (mem.append 1))
  rst)

(sol 100)
