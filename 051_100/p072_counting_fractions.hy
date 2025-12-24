;;; hy==1.0a4

(import time [time])

(defn solution [[D 1_000_000]]
  (setv sieve (* [True] (+ D 1))
        phi (list (range (+ D 1))))
  (for [d (range 2 (+ D 1))]
    (when (get sieve d)
      (-= (get phi d) 1)
      (for [i (range (* 2 d) (+ D 1) d)]
        (setv (get sieve i) False)
        (//= (get phi i) d)
        (*= (get phi i) (- d 1)))))
  (sum (cut phi 2 None)))

(defn main []
  (setv start (time))
  (print (solution))
  (print "elapsed:" (- (time) start)))

(main)


