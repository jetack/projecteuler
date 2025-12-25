;;; hy==1.0a4

(import time [time])

(defn prime? [n]
  (if (= 0 (% n 2))
      False
      (do (setv d 3)
          (while (<= (* d d) n)
            (if (= (% n d) 0)
                (return False))
            (+= d 2))
          True)))

(defn ratio [cnt n]
  (/ cnt (+ (* 4 n) 1)))

(defn sol [thr]
  (setv cnt 3
        n 1
        cur 9)
  (while (> (ratio cnt n) thr)
    (+= n 1)
    (for [_ (range 3)]
      (+= cur (* 2 n))
      (if (prime? cur)
          (+= cnt 1)))
    (+= cur (* 2 n)))
  (+ 1 (* 2 n)))

(setv t (time))
(print (sol 0.1))
(print (- (time) t))

;;; 600ms in pypy
