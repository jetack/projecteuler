;;; hy==1.0a4

(import time [time])

(defn gcd [a b]
  (if (> a b)
      (setv [a b] [b a]))
  (while a
    (setv [a b] [(% b a) a]))
  b)

(defn solution [[D 12000]]
  (setv rst 0)
  (for [d (range 4 (+ D 1))]
    (for [n (range (- d (// (* 2 d) 3)) (- d (// d 2)))]
      (if (= (gcd n d) 1) (+= rst 1))))
  rst)

(defn main []
  (setv start (time))
  (print (solution))
  (print "elapsed:" (- (time) start)))

(main)
