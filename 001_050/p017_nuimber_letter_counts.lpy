(setv d {1 "one"
         2 "two"
         3 "three"
         4 "four"
         5 "five"
         6 "six"
         7 "seven"
         8 "eight"
         9 "nine"
         10 "ten"
         11 "eleven"
         12 "twelve"
         13 "thirteen"
         14 "fourteen"
         15 "fifteen"
         16 "sixteen"
         17 "seventeen"
         18 "eighteen"
         19 "nineteen"
         20 "twenty"
         30 "thirty"
         40 "forty"
         50 "fifty"
         60 "sixty"
         70 "seventy"
         80 "eighty"
         90 "ninety"
         1000 "onethousand"})

(defn update-hundreds [mem]
  (for [i (range 100 (min (len mem) 1000) 100)]
    (setv (get mem i) (+ (get mem (// i 100))
                         "hundred"))))

(defn update-under-hundred [mem]
  (for [i (range 20 (min (len mem) 100) 10)]
    (for [j (range 1 (min (- (len mem) i) 10))]
      (setv (get mem (+ i j)) (+ (get mem i)
                                 (get mem j))))))

(defn update-under-thousand [mem]
  (for [i (range 100 (min (len mem) 1000) 100)]
    (for [j (range 1 (min 100 (- (len mem) i)))]
      (setv (get mem (+ i j)) (+ (get mem i)
                                 "and"
                                 (get mem j))))))

(defn sol [s e]
  (setv mem (* [""] (+ e 1)))
  (for [(, k v) (d.items)]
    (if (<= k e)
        (setv (get mem k) v)))
  (update-hundreds mem)
  (update-under-hundred mem)
  (update-under-thousand mem)
  mem)

(setv mem (sol 1 1000))

(print (reduce + (lfor s mem (len s))))
