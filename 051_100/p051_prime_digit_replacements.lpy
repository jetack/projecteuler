;;; hy==1.0a4

(import time [time]
        collections [defaultdict])

(defn num-to-patterns [n]
  (setv rst []
        ns (str n))
  (defn recur [s c rst [depth 0]]
    (if (= depth (len s))
        (return rst))
    (when (= (get s depth) c)
      (setv new [])
      (for [pattern rst]
        (new.append (+ (cut pattern None depth)
                       "*"
                       (cut pattern (+ depth 1) None))))
      (+= rst new))
    (recur s c rst (+ depth 1)))
  (for [c "0123456789"]
    (+= rst (cut (recur ns c [ns]) 1 None)))
  rst)

(defn get-next-p [primes]
  (setv n (+ (get primes -1) 2))
  (while True
    (for [p primes]
      (cond [(> (* p p) n) (return n)]
            [(= 0 (% n p)) (break)]))
    (+= n 2)))

(defn solution [[n 8]]
  (setv pattern-mem (defaultdict list)
        primes [2 3 5]
        (get pattern-mem "*") [2 3 5])
  (while True
    (setv p (get-next-p primes))
    (primes.append p)
    (for [pattern (num-to-patterns p)]
      (setv mem-lst (get pattern-mem pattern))
      (.append mem-lst p)
      (if (= n (len mem-lst))
          (return mem-lst)))))

(defn main []
  (setv start (time))
  (print (solution))
  (print "elapsed:" (- (time) start)))

(main)
