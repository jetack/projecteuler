(defn sol []
  (setv ret None)
  (for [i (range 999 99 -1)]
    (for [j (range 999 99 -1)]
      (setv n (* i j)
            s (str n))
      (if (and (= s (get s (slice None None -1)))
               (or (is ret None)
                   (> n ret)))
          (setv ret n))))
  ret)

(sol)
