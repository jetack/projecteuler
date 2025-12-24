;;; hy==1.0a4

(import time [time])

(defn solution [[n 100]]
  (setv mem [[1]
             [0 1]])
  (for [i (range 2 (+ n 1))]
    (setv partitions [0]
          partial-sum 0)
    (for [j (range 1 (+ i 1))]
      (+= partial-sum (get (get mem (- i j)) (min j (- i j))))
      (partitions.append partial-sum))
    (mem.append partitions))
  (get (get mem -1) -2))

(defn main []
  (setv start (time))
  (print (solution 100))
  (print "elapsed:" (- (time) start)))

(main)
