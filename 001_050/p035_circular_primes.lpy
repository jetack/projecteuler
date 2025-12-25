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

(defn all-circular [p]
  (setv ret #{p}
        p-str (str p))
  (if (in "0" p-str)
      (return (set)))
  (for [i (range 1 (len p-str))]
    (ret.add (int (+ (get p-str (slice i None))
                     (get p-str (slice None i))))))
  ret)

(defn find-circular-primes [primes]
  (setv ret (set))
  (for [p (list primes)]
    (setv circulars (all-circular p))
    (when (and circulars (not (lfor c circulars :if (not (in c primes)) c)))
      (setv ret (ret.union circulars)))
    (-= primes circulars))
  ret)

(print (len (find-circular-primes (build-primes (** 10 6)))))
