(defn cycle-len [n]
  (setv mem (* [-1] n)
        cur 0
        remain 1)
  (while remain
    (if (!= (get mem remain) -1)
        (return (- cur (get mem remain)))
        (setv (get mem remain) cur))
    (*= remain 10)
    (%= remain n)
    (+= cur 1))
  0)

(defn sol [d]
  (setv M 0
        ret 0)
  (for [i (range 2 d)]
    (setv l (cycle-len i))
    (if (> l M)
        (do (setv M l
                  ret i))))
  ret)

(sol 1000)
