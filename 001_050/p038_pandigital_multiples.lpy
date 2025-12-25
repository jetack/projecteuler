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
(defn num-to-set [n]
  (setv ret (set))
  (while n
    (ret.add (% n 10))
    (//= n 10))
  ret)

(defn propagate [p]
  (setv ret (str p)
        i 2)
  (while (< (len ret) 9)
    (+= ret (str (* p i)))
    (+= i 1))
  (int ret))

(defn pandigital? [n [l 9]]
  (and (= (len (str n)) l)
       (= (num-to-set n) (set (range 1 (+ 1 l))))))

(setv candidates (set (range 1 10)))

(print (travel-permutation
         ;; since n > 1, lengths < 5
         [[candidates candidates] [lengths (range 1 5)] [ret 0]]
         (setv p (lst-to-num perm)
               prop (propagate p))
         (when (pandigital? prop)
           (setv ret (max ret prop)))))
