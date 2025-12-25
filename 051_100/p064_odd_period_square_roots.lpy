;;; hy==1.0a4

(import time [time])

(defn get-period [n a]
  (setv mem (dict)
        b 1
        step 0)
  (while True
    (if (in (, a b) mem)
        (return (- step (get mem (, a b))))
        (setv (get mem (, a b)) step))
    (setv b (// (- n (** a 2)) b)
          a (- a))
    (while (<= (** a 2) n)
      (+= a b))
    (-= a b)
    (+= step 1)))

(defn solution [N]
  (setv rst 0
        a 1)
  (while True
    (for [i (range (+ (** a 2) 1) (** (+ a 1) 2))]
      (if (> i N) (return rst))
      (if (% (get-period i a) 2)
          (+= rst 1)))
    (+= a 1))
  rst)

(defn main []
  (setv start (time))
  (print (solution 10000))
  (print "elapsed:" (- (time) start)))

(main)
