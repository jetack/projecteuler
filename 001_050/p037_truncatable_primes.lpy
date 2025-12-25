;;; build-primes from 27
(defn build-primes [n]
  (setv sieve (* [True] n))
  (for [i (range 2)]
    (setv (get sieve i) False))
  (for [i (range 2 n)]
    (if (get sieve i)
        (for [j (range (* 2 i) n i)]
          (setv (get sieve j) False))))
  (sfor i (range n) :if (get sieve i) i))


(defn truncatable? [p primes]
  (if (< p 10)
      False
      (and (left-truncatable? p primes)
           (right-truncatable? p primes))))

(defn right-truncatable? [p primes]
  (while p
    (if (not (in p primes))
        (return False))
    (//= p 10))
  True)

(defn left-truncatable? [p primes]
  (setv d 1)
  (while (<= d p)
    (*= d 10))
  (while p
    (if (not (in p primes))
        (return False))
    (//= d 10)
    (%= p d))
  True)

(defn truncatable-primes [n]
  (setv primes (build-primes n))
  (lfor p (sorted (list primes)) :if (truncatable? p primes) p))

(defmacro do-while [#* args]
  (setv body (get args (slice None -1))
        condition (get args -1))
  `(do
     ~@body
     (while ~condition
       ~@body)))

(defn sol [n]
  (setv l 100)
  (do-while
    (setv lst (truncatable-primes l))
    (*= l 10)
    ;; while
    (< (len lst) n))
  (print l)
  (sum lst))

(sol 11)

;; result is 
;; 10000000
;; 748317
;; thus, (len (truncatable-primes 1000000)) should be the answer
