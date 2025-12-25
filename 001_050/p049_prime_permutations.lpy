(import [collections [defaultdict]])

(defn build-primes [primes limit]
  (for [i (range (+ (get primes -1) 2) limit 2)]
    (for [p primes]
      (cond [(> (* p p) i) (do (primes.append i) (break))]
            [(= 0 (% i p)) (break)])))
  primes)

(defn build-dict [primes d]
  (setv rst (defaultdict list))
  (for [p primes]
    (if (> p (** 10 (- d 1)))
        (.append (get rst (.join "" (sorted (list (str p))))) p)))
  rst)

(defn find-sequence [lst]
  (setv rst [])
  (for [i (range (- (len lst) 2))]
    (for [j (range (+ i 1) (- (len lst) 1))]
      (setv iv (get lst i)
            jv (get lst j))
      (if (in (+ jv (- jv iv)) lst)
          (rst.append [iv jv (+ jv (- jv iv))]))))
  rst)

(defn wanted-form [lst]
  (.join "" (map str lst)))

(defn sol [d]
  (setv primes (build-primes [2 3] (** 10 d))
        categorized (build-dict primes d))
  (for [[digits d-primes] (categorized.items)]
    (setv found (find-sequence d-primes))
    (if found
        (for [seq found]
          (print (wanted-form seq))))))

(sol 4)
