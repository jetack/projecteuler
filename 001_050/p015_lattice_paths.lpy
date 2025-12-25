(import [hy.contrib.loop [__trampoline__]])

(defmacro/g! defn-recur [fn-name args #* body]
  `(with-decorator __trampoline__
     (defn ~fn-name ~args
       ~@body)))

(defn comb [n k]
  (defn-recur recur [n k [ret 1] [i 1]]
        (if (> i k)
            ret
            (recur (- n 1) k (-> ret (* n) (// i)) (+ i 1))))
  (recur n (min k (- n k))))

(comb 40 20)
