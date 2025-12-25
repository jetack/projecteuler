(defn prime? [primes i]
  (for [p primes]
    (cond [(= 0 (% i p)) (return False)]
          [(> (* p p) i) (return True)]))
  True)

(defn goldbach? [i prime-set]
  (setv j 1)
  (while (<= (+ 2 (* 2 (* j j))) i)
    (if (in (- i (* 2 (* j j))) prime-set)
        (return True))
    (+= j 1))
  False)

(defn sol []
  (setv primes [2]
        prime-set (set primes)
        i 3)
  (while True
    (if (prime? primes i)
        (do (primes.append i)
            (prime-set.add i))
        (if (not (goldbach? i prime-set))
            (return i)))
    (+= i 2)))
(sol)
