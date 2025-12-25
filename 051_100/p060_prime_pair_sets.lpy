;;; hy==1.0a4

(import time [time]
        collections [deque])

(defn prime? [n primes]
  (for [p primes]
    (cond [(= (% n p) 0) (return False)]
          [(> (* p p) n) (return True)]))
  True)

(defn sieve [n]
  (setv prime? (* [True] n))
  (for [i (range 4 n 2)]
    (setv (get prime? i) False))
  (for [i (range 3 n 2)]
    (if (> (* i i) n)
        (break))
    (for [j (range (* 2 i) n i)]
      (setv (get prime? j) False)))
  (+ [2] (lfor i (range 3 n 2) :if (get prime? i) i)))

(defn int-concat [a b]
  (+ (* a (** 10 (len (str b)))) b))

(defn satisfies [lst compatibles]
  (for [i lst]
    (if (not (in i compatibles))
        (return False)))
  True)

(defn solution [[n 5]]
  (setv primes (sieve 100000)
        mem (lfor i (range n) [])
        rst (float "inf"))
  (for [p primes]
    (if (> p rst) (break))
    (setv compatibles (sfor i primes :if (and (< i p)
                                              (prime? (int-concat i p) primes)
                                              (prime? (int-concat p i) primes))
                            i))
    (for [i compatibles]
      (.append (get mem 2) [i p]))
    (for [lst (get mem (- n 1))]
      (if (satisfies lst compatibles)
          (setv rst (min rst (+ (sum lst) p)))))
    (for [i (range (- n 2) 1 -1)]
      (for [lst (get mem i)]
        (if (satisfies lst compatibles)
            (.append (get mem (+ i 1)) (+ lst [p]))))))
  rst)

(defn main []
  (setv start (time))
  (print (solution 5))
  (print "elapsed:" (- (time) start)))

(main)
