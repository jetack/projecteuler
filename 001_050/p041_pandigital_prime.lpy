(defn build-primes [n]
  (setv sieve (* [True] n))
  (for [i (range 2)]
    (setv (get sieve i) False))
  (for [i (range 2 n)]
    (if (get sieve i)
        (for [j (range (* 2 i) n i)]
          (setv (get sieve j) False))))
  (lfor i (range n) :if (get sieve i) i))

(defn prime? [n primes]
  (for [p primes]
    (cond [(> (* p p) n) (return True)]
          [(= (% n p) 0) (return False)]))
  True)

(defmacro/g! travel-permutation [bindings #* body]
  (setv [argsymbols argvalues] (if bindings (zip #* bindings) [[] []]))
  (for [[i s] (enumerate ["candidates" "lengths"])]
    (assert (= (hy.models.Symbol s) (get argsymbols i))))
  `(do
     (defn g!fn [~@argsymbols]
       (setv perm []
             terminate []
             max-depth (max lengths)
             lengths (set lengths))
       (defn ~g!recur [perm terminate ~@argsymbols [l 0] [d max-depth]]
         (when (not terminate)
           (when (in l lengths)
             ~@body)
           (when d
             (for [c (list candidates)]
               (perm.append c)
               (candidates.remove c)
               (setv ret (~g!recur perm terminate ~@argsymbols (+ l 1) (- d 1)))
               (candidates.add c)
               (perm.pop))))
         ret)
       (~g!recur perm terminate ~@argvalues))
     (g!fn ~@argvalues)))


(defn lst-to-num [lst]
  (setv ret 0)
  (for [d lst]
    (*= ret 10)
    (+= ret d))
  ret)

(defn sol [n]
  (setv primes (build-primes (** 10 (+ 1 (// n 2))))
        ret 0
        i n)
  (while (not ret)
    (setv ret (travel-permutation
                [[candidates (set (range 1 (+ 1 i)))] [lengths [i]] [primes primes] [ret 0]]
                (setv p (lst-to-num perm))
                (when (prime? p primes)
                  (setv ret (max ret p)))))
    (-= i 1))
  ret)

(sol 9)
