(import time
        [collections [defaultdict]]
        [hy.contrib.loop [__trampoline__]])

(defn prime? [n all-p-below]
  (for [p all-p-below]
    (cond [(> (* p p) n) (break)]
          [(= 0 (% n p)) (return False)]))
  True)

;; ;;; while version
;; (defn prime-update [n [primes None]]
;;   (if (is primes None)
;;       (setv primes [2 3]))
;;   (setv i (+ (get primes -1) 2))
;;   (while (<= (* i i) n)
;;     (if (prime? i primes)
;;         (primes.append i))
;;     (+= i 2))
;;   primes)

;; ;;; exactly same behavior but slow. don't use loop/recur. make sol 500 times slower than while-version
;; (defn prime-update [n [primes None]]
;;   (if (is primes None)
;;       (setv primes [2 3]))
;;   (loop [[i (+ (get primes -1) 2)]]
;;         (if (> (* i i) n)
;;             (return primes))
;;         (do (if (prime? i primes)
;;                 (primes.append i))
;;             (recur (+ i 2)))))

;;; trampoline decorator version. I prefer this.
(defn prime-update [n [primes None]]
  (if (is primes None)
      (setv primes [2 3]))
  (with-decorator __trampoline__
    (defn recur [i]
      (if (> (* i i) n) (return primes))
      (if (prime? i primes) (primes.append i))
      (recur (+ i 2))))
  (recur (+ (get primes -1) 2)))


(defn exponents [n primes]
  (setv ret (defaultdict int))
  (for [(, _ p) (enumerate primes)]
    (if (> (* p p) n) (break))
    (while (= 0 (% n p))
      (+= (get ret p) 1)
      (//= n p)))
  (if (> n 1) (+= (get ret n) 1))
  ret)

(defn merge-exponents [e1 e2]
  (for [(, k v) (e2.items)]
    (+= (get e1 k) v))
  e1)

(defn count-div [exponents]
  (reduce * (lfor (, _ v) (exponents.items) (+ v 1))))

(defn sol [n]
  (setv primes [2 3]
        i 2
        num-div -1)
  (while (<= num-div n)
    (prime-update (+ i 1) primes)
    (setv (, a b) (, i (+ i 1)))
    (if (% i 2) (//= b 2) (//= a 2))
    (setv num-div (count-div (merge-exponents (exponents a primes)
                                              (exponents b primes))))
    (+= i 1))
  (* a b))

(setv t (time.time))
(print (sol 2000))
(print (- (time.time) t))
