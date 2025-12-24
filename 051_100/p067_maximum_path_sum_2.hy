(defn parse [lst]
  (lfor l lst (lfor d (l.split " ") (int d))))

(defn sol [parsed]
  (for [i (range (- (len parsed) 2) -1 -1)]
    (setv (get parsed i) (lfor (, j d) (enumerate (get parsed i))
                               (+ d (max (get (get parsed (+ i 1)) j) (get (get parsed (+ i 1)) (+ j 1)))))))
  (get (get parsed 0) 0))

(defn load-inputs [path]
  (with [f (open path "r")]
    (f.readlines)))

(sol (parse (load-inputs "./p067_triangle.txt")))
