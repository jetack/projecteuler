;;; hy==1.0a4

(import time [time]
        collections [defaultdict]
        functools [reduce])

(defn solution []
  (setv dicts (lfor i (range 6) (defaultdict list)))
  (for [i (range 6)]
    (setv n 1
          p 1)
    (while (< p 1000)
      (+= p (+ 1 (* (+ i 1) n)))
      (+= n 1))
    (while (< p 10000)
      (.append (get (get dicts i) (// p 100)) p)
      (+= p (+ 1 (* (+ i 1) n)))
      (+= n 1)))
  (defn search [mask hist]
    (if (and (= mask 0) (= (// (get hist 0) 100) (% (get hist -1) 100)))
        (return hist))
    (for [i (range 6)]
      (if (& mask (<< 1 i))
          (if hist
              (for [p (get (get dicts i) (% (get hist -1) 100))]
                (setv rst (search (^ mask (<< 1 i)) (+ hist [p])))
                (if rst (return rst)))
              (for [[k v] (.items (get dicts i))]
                (for [p v]
                  (setv rst (search (^ mask (<< 1 i)) (+ hist [p])))
                  (if rst (return rst))))))))
  (sum (search (- (<< 1 6) 1) [])))

(defn main []
  (setv start (time))
  (print (solution))
  (print "elapsed:" (- (time) start)))

(main)
