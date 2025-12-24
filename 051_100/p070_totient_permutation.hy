;;; hy==1.0a4

(import time [time])

(defn perm? [n phi]
  (= (sorted (str n))
     (sorted (str phi))))

(defn solution [[D 10_000_000]]
  (setv sieve (* [True] (+ D 1))
        phi (list (range (+ D 1)))
        [a b] [87109 79180])
  (for [d (range 2 (+ D 1))]
    (when (get sieve d)
      (-= (get phi d) 1)
      (for [i (range (* 2 d) (+ D 1) d)]
        (setv (get sieve i) False)
        (//= (get phi i) d)
        (*= (get phi i) (- d 1)))))
  (for [i (range 2 (+ D 1))]
    (if (and (perm? i (get phi i)) (< (* i b) (* (get phi i) a)))
        (setv [a b] [i (get phi i)])))
  a)

(defn main []
  (setv start (time))
  (print (solution))
  (print "elapsed:" (- (time) start)))

(main)
