(import [time [time]])

(defn sol [n]
  (setv primes [2]
        i 3
        cnt n)
  (while True
    (setv j i)
    (setv factors 0)
    ;; count prime factors
    (for [p primes]
      (if (> (* p p) j)
          (break))
      (if (= 0 (% j p))
          (+= factors 1))
      (while (= 0 (% j p))
        (//= j p)))
    (if (and factors (> j 1))
        (+= factors 1))
    ;; if i has n factors
    (if (= factors n)
        (-= cnt 1)
        (setv cnt n))
    ;; if n consecutive numbers found
    (if (= 0 cnt)
        (return (- i (- n 1))))
    ;; if i is prime
    (if (= factors 0)
        (primes.append i))
    (+= i 1)))

(setv t (time))
(print (sol 4))
(print (- (time) t))
