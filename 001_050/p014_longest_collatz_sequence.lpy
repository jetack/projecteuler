(defn next-term [n]
  (if (% n 2)
      (+ (* 3 n) 1)
      (// n 2)))

(defn sol [n]
  (setv mem {})
  ;; deal with power of 2
  (setv i 1
        l 1)
  (while (< i n)
    (setv (get mem i) l)
    (+= l 1)
    (<<= i 1))
  ;; deal with others
  (for [i (range 1 n)]
    (setv j i
          stack [])
    (while (and (> j 1) (not (in j mem)))
      (stack.append j)
      (setv j (next-term j)))
    (setv l (get mem j))
    (while stack
      (+= l 1)
      (setv (get mem (stack.pop)) l)))
  ;; find longest
  (setv ret 0
        M 0)
  (for [i (range 1 n)]
    (if (> (get mem i) M)
        (setv (, ret M) (, i (get mem i)))))
  ret)

(sol (** 10 6))
