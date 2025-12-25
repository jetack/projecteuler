(require [hy.contrib.loop [loop]])

(setv n (* 2 (** 10 6)))

(defn is-prime? [n all-p-below]
  (for [p all-p-below]
    (cond [(> (* p p) n) (break)]
          [(= 0 (% n p)) (return False)]))
  True)

(defn build-primes [n]
  (loop [[i 3] [primes [2]]]
        (if (>= i n)
            primes
            (do (if (is-prime? i primes)
                    (primes.append i))
                (recur (+ i 2) primes)))))

(sum (build-primes n))
