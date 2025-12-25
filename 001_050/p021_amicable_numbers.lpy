(defn eratosthenes [n]
  (setv mem (* [1] n))
  (for [i (range 2 n)]
    (for [j (range (* 2 i) n i)]
      (+= (get mem j) i)))
  mem)

(defn sol [n]
  (setv ret 0
        mem (eratosthenes n))
  (for [i (range n)]
    (for [j (range (+ i 1) n)]
      (if (and (= i (get mem j))
               (= j (get mem i)))
          (+= ret (+ i j)))))
  ret)

(sol 10000)
