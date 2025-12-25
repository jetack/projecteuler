(defn recur [amount cur coins]
  (setv coin (get coins cur)
        cnt 0)
  (if (= cur 0)
      (= (% amount coin) 0)
      (do (for [i (range (+ (// amount coin) 1))]
            (+= cnt (recur (- amount (* i coin)) (- cur 1) coins)))
          cnt)))

(defn sol [amount coins]
  (recur amount (- (len coins) 1) coins))

(sol 200 [1 2 5 10 20 50 100 200])
