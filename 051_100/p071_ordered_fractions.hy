;;; hy==1.0a4

(import time [time])

(defn gcd [a b]
  (if (> a b)
      (setv [a b] [b a]))
  (while a
    (setv [a b] [(% b a) a]))
  b)

(defn solution [[D 1_000_000]]
  (setv [a b] [0 1]
        [rn rd] [3 7])
  (for [d (range 2 (+ D 1))]
    (for [n (range (- (// (* rn d) rd) (= 0 (% (* rn d) rd))) (// (* a d) b) -1)]
      (if (> (gcd n d) 1)
          (continue)
          (do (setv [a b] [n d])
              (break)))))
  [a b])

(defn main []
  (setv start (time))
  (print (solution))
  (print "elapsed:" (- (time) start)))

(main)


