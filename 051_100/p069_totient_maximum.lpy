;;; hy==1.0a4

(defn prime? [n primes]
  (for [p primes]
    (cond [(> (* p p) n) (return True)]
          [(= (% n p) 0) (return False)])))

(defn prime-generator []
  (setv primes [2]
        last-prime 3)
  (yield 2)
  (while True
    (while (not (prime? last-prime primes))
      (+= last-prime 2))
    (primes.append last-prime)
    (yield last-prime)
    (+= last-prime 2)))

(defn sol [n]
  (setv rst 1
        p-gen (prime-generator))
  (while True
    (setv p (next p-gen))
    (if (<= (* rst p) n)
        (*= rst p)
        (break)))
  rst)

(print (sol (** 10 6)))
