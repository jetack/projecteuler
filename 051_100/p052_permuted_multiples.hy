(defn condition? [n]
  (setv digit-set (set (str n)))
  (if (!= (len digit-set)
          (len (str n)))
      (return False))
  (for [i (range 2 7)]
    (if (!= (set (str (* i n)))
            digit-set)
        (return False)))
  True)

(setv i 1)
(while (not (condition? i))
  (+= i 1))
(print i)
