(defn prime? [primes i]
  (for [p primes]
    (cond [(= 0 (% i p)) (return False)]
          [(> (* p p) i) (return True)]))
  True)

(defn build-primes [n]
  (setv primes [2])
  (for [i (range 3 n 2)]
    (if (prime? primes i)
        (primes.append i)))
  primes)

(defn get-pfsum [lst]
  (setv rst (+ [0] lst))
  (for [i (range (len lst))]
    (+= (get rst (+ i 1)) (get rst i)))
  rst)

(defn sol [n]
  (setv primes (build-primes n)
        pfsum (get-pfsum primes)
        prime-set (set primes)
        rst 0
        max-len 0)
  (for [i (range (len primes))]
    (for [j (range (+ i 1) (len pfsum))]
      (setv consec (- (get pfsum j) (get pfsum i)))
      (cond [(> consec n) (break)]
            [(and (in consec prime-set)
                  (> (- j i) max-len))
             (setv [rst max-len] [consec (- j i)])])))
  rst)

(sol 1000000)
