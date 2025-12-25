(import [hy.contrib.loop [__trampoline__]])

(defn add-arr [a b]
  (setv remain 0
        ret [])
  (for [i (range (len a))]
    (setv s (+ (get a i)
               (get b i)
               remain))
    (ret.append (% s 10))
    (setv remain (// s 10)))
  (for [j (range (len a) (len b))]
    (setv s (+ (get b j)
               remain))
    (ret.append (% s 10))
    (setv remain (// s 10)))
  (while remain
    (ret.append (% remain 10))
    (//= remain 10))
  ret)

(with-decorator __trampoline__
  (defn recur [a b d [n 1]]
    (if (>= (len a) d)
        n
        (recur b (add-arr a b) d (+ n 1)))))


(defn sol [d]
  (recur [1] [1] d))

(sol 1000)
