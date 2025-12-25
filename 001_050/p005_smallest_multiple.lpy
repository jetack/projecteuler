(defn all-primes-till [n]
  (setv sieve (+ (* (min 2 n) [0]) (* (- n 1) [1])))
  (for [i (range 2 (+ n 1))]
    (for [j (range (* 2 i) (+ n 1) i)]
      (setv (get sieve j) 0)))
  (lfor i (range (+ n 1)) :if (get sieve i) i))

(defn sol [n]
  (setv ret 1)
  (for [p (all-primes-till n)]
    (setv f 1)
    (while (<= f (/ n p))
      (*= f p))
    (*= ret f))
  ret)

(sol 20)
