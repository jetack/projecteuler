(defn build-primes [n]
  (setv sieve (* [True] n))
  (for [i (range 2)]
    (setv (get sieve i) False))
  (for [i (range 2 n)]
    (if (get sieve i)
        (for [j (range (* 2 i) n i)]
          (setv (get sieve j) False))))
  (sfor i (range n) :if (get sieve i) i))

(defn quad-form [a b]
  (fn [x] (+ (* x x) (* a x) b)))


(defn count-combo [f primes]
  (setv i 0)
  (while (in (f i) primes)
    (+= i 1))
  i)


(defn sol [am bm]
  (setv M 0
        i am
        j bm
        primes (build-primes (+ (max am bm) 1)))
  (for [a (range (- am) (+ am 1))]
    (for [b (range 2 (+ bm 1))]
      (setv combo (count-combo (quad-form a b) primes))
      (if (> combo M)
          (do (setv M combo
                    i a
                    j b)))))
  (* i j))

(sol 1000 1000)
