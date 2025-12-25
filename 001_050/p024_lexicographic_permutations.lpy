(import [hy.contrib.loop [__trampoline__]])

(setv ordered [0 1 2 3 4 5 6 7 8 9])

(with-decorator __trampoline__
  (defn fact [n [ret 1]]
    (if (< n 2)
        ret
        (fact (- n 1) (* ret n)))))

;;; better way. tail-call recursion.
(defn sol [n ordered]
  (setv l (len ordered)
        mark (* [False] l))
  (with-decorator __trampoline__
    (defn recur [[depth (- l 1)] [step-size (fact (- l 1))] [n n] [ret ""] [mark mark]]
      (if (= depth 0)
          (do (setv i 0)
              (while (get mark i)
                (+= i 1))
              (+ ret (str (get ordered i))))
          (do (setv i 0)
              (while (get mark i)
                (+= i 1))
              (while (> n step-size)
                (-= n step-size)
                (+= i 1)
                (while (get mark i)
                  (+= i 1)))
              (setv d (get ordered i))
              (setv (get mark i) True)
              (recur (- depth 1) (// step-size depth) n (+ ret (str d)) mark)))))
  (recur))


;;; brute-force with recursion
;; (defn sol [n]
;;   (defn recur [hist n [depth (- (len ordered) 1)] [cnt 0]]
;;     (if (= depth 0)
;;         (for [d ordered]
;;           (if (in d hist) (continue))
;;           (return (, (str d) 1)))
;;         (do (for [d ordered]
;;               (if (in d hist) (continue))
;;               (hist.add d)
;;               (setv (, s diff) (recur hist (- n cnt) (- depth 1)))
;;               (+= cnt diff)
;;               (if (= n cnt)
;;                   (return (, (+ (str d) s) n)))
;;               (hist.remove d))
;;             (return (, None cnt)))))
;;   (get (recur (set) n) 0))


(sol (** 10 6) ordered)
