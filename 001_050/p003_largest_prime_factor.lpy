(setv n 600851475143)

(defn sol [n]
  (setv ret (if (% n 2)
                1
                (do (while (= 0 (% n 2))
                      (//= n 2))
                    2))
        i 3)
  (while (<= i n)
    (if (= 0 (% n i))
        (do (setv ret i)
            (while (= 0 (% n i)) (//= n i))))
    (+= i 2))
  ret)

(sol n)
