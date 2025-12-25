;;; hy==1.0a4
;;; Cpython 27s, pypy 800ms

(defn tco [f]
  (setv active False
        stored False
        argstore None)
  (fn [#* args]
    (nonlocal active stored argstore)
    (setv argstore args)
    (setv stored True)
    (when (not active)
      (setv active True)
      (while stored
        (setv stored False)
        (setv result (f #* argstore)))
      (setv active False)
      result)))

(import functools [lru_cache]
        time [time])

(defn square-digit-sum [n]
  (setv rst 0)
  (while n
    (+= rst (** (% n 10) 2))
    (//= n 10))
  rst)

(with-decorator tco
  (defn which-chain? [ds]
    (if (or (= ds 1) (= ds 89))
        ds
        (which-chain? (square-digit-sum ds)))))

(with-decorator (lru_cache :maxsize None)
  (defn cached-which-chain? [ds]
    (which-chain? ds)))

(defn sol [n]
  (setv rst 0)
  (for [i (range 1 n)]
    (if (= 89 (cached-which-chain? (square-digit-sum i)))
        (+= rst 1)))
  rst)

(setv t (time))
(print (sol (** 10 7)))
(print (- (time) t))
