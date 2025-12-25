(defn same-fraction? [ni di nj dj]
  (= (* di nj) (* ni dj)))

(defn digit-cancellable? [i j k l]
  (setv numer (+ (* 10 i) j)
        denom (+ (* 10 k) l))
  (if (and (or (and (= i k) (same-fraction? numer denom j l))
               (and (= i l) (same-fraction? numer denom j k))
               (and (= j k) (same-fraction? numer denom i l))
               (and (= j l) (same-fraction? numer denom i k)))
           (* i j k l))
      True
      False))

(defn gcd [a b]
  (setv [a b] [(min a b) (max a b)])
  (while a
    (setv [a b] [(% b a) a]))
  b)

(defn sol []
  (setv numer 1
        denom 1)
  (for [d (range 10 100)]
    (for [n (range 10 d)]
      (if (digit-cancellable? (// n 10) (% n 10) (// d 10) (% d 10))
          (do (*= numer n)
              (*= denom d)))))
  (// denom (gcd numer denom)))

(print (sol))
