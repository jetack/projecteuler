;;; hy==1.0a4

(import time [time])

(defn next-p [primes]
  (setv c (get primes -1))
  (while True
    (+= c 2)
    (for [p primes]
      (if (= (% c p) 0)
          (break))
      (if (> (* p p) c) (return c)))))

(defn solution [[N 5000]]
  (setv mem [[1]
             [0 0]]
        primes [2 3]
        n 2)
  (while True
    (while (< (get primes -1) n)
      (primes.append (next-p primes)))
      (setv partitions (* [0] (+ n 1))
            partial-sum 0)
    (for [p primes]
      (if (> p n) (break))
      (+= partial-sum (get (get mem (- n p)) (min p (- n p))))
      (setv (get partitions p) partial-sum))
    (if (> partial-sum N) (break))
    (setv (get partitions n) partial-sum)
    (mem.append partitions)
    (+= n 1))
  n)

(defn main []
  (setv start (time))
  (print (solution))
  (print "elapsed:" (- (time) start)))

(main)
