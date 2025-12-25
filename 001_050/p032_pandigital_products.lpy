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

(defn factors-found? [p candidates]
  (travel-permutation
    ;; assume multiplicand < multiplier, length of multiplicand lies in [1 2]
    [[candidates candidates] [lengths [1 2]] [p p] [ret False]]
    (setv m (lst-to-num perm))
    (when (and (= (% p m) 0) (= candidates (num-to-set (// p m))))
      (setv ret True)
      (terminate.append True))))

(setv candidates (set (range 1 10)))

(print (sum (travel-permutation
              ;; since (* 99 99) < 11111, (* 111 111), (* 11 111), (1 1111) > 9 product should be length of 4
              [[candidates candidates] [lengths [4]] [ret []]]
              (setv p (lst-to-num perm))
              (when (factors-found? p candidates)
                (ret.append p)))))
