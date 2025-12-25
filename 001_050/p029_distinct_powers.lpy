(defn build-primes [n]
  (setv sieve (* [True] n))
  (for [i (range 2)]
    (setv (get sieve i) False))
  (for [i (range 2 n)]
    (if (get sieve i)
        (for [j (range (* 2 i) n i)]
          (setv (get sieve j) False))))
  (sfor i (range n) :if (get sieve i) i))

(defn factorize [n primes]
  (setv ret (* [0] (len primes)))
  (for [(, i p) (enumerate primes)]
    (while (= 0 (% n p))
      (//= n p)
      (+= (get ret i) 1)))
  ret)

(defn coord-to-str [coord]
  (.join " " (map str coord)))

(defn power-coord [coord e]
  (lfor c coord (* e c)))

(defn sol [n]
  (setv mem (set))
  (setv primes (build-primes (+ n 1)))
  (for [a (range 2 (+ n 1))]
    (for [b (range 2 (+ n 1))]
      (mem.add (coord-to-str (power-coord (factorize a primes) b)))))
  (len mem))

(sol 100)
