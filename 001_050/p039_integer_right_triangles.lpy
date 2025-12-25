(defn criterion [a b c]
  (- (+ (* a a) (* b b)) (* c c)))

(defn num-solutions [p]
  (setv ret 0)
  (for [i (range 1 (// p 3))]
    (for [j (range (+ i 1) (// (* p 2) 3))]
      (setv c (criterion i j (- p i j)))
      (cond [(= c 0) (+= ret 1)]
            [(> c 0) (break)])))
  ret)

(max (lfor i (range 3 1001) [(num-solutions i) i]))
