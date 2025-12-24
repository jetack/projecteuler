;;; hy==1.0a4

(import time [time]
        collections [defaultdict])

(defn n2i [n]
  (.join "" (sorted (str n))))

(defn solution [[n 5]]
  (setv i2lst (defaultdict list)
        i 0
        l 1)
  (while True
    (+= i 1)
    (setv cubic (** i 3)
          idx (n2i cubic))
    (when (> (len idx) l)
      (setv found (lfor [j v] (i2lst.items) :if (= (len v) n) (get v 0))
            i2lst (defaultdict list)
            l (len idx))
      (if found (return (min found))))
    (.append (get i2lst (n2i cubic)) cubic)))

(defn main []
  (setv start (time))
  (print (solution))
  (print "elapsed:" (- (time) start)))

(main)
