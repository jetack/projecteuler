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

(setv candidates (set (range 10)))

(sum (travel-permutation
       [[candidates candidates] [lengths [4 5 6 7 8 9 10]] [ret []] [primes [2 3 5 7 11 13 17]]]
       (setv p (lst-to-num (get perm (slice -3 None))))
       (if (% p (get primes (- l 4)))
           (return ret))
       (if (= l 10)
           (ret.append (lst-to-num perm)))))
