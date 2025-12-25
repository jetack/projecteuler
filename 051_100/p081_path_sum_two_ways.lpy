;;; hy==1.0a4

(import hyrule *)
(require hyrule *)

(import functools [cache])



(defn parse [path]
  (with [f (open path "r")]
    (lfor line (f.readlines) (as-> line x
                                   (x.strip)
                                   (x.split ",")
                                   (map int x)
                                   (list x)))))

(defn sol [path]
  (setv mat (parse path))
  #@(cache
      (defn min-path [i j]
        (setv prevs [])
        (if (> i 0)
            (prevs.append (min-path (- i 1) j)))
        (if (> j 0)
            (prevs.append (min-path i (- j 1))))
        (+ (get (get mat i) j) (if prevs (min prevs) 0))))
  (min-path 79 79))

(sol "./p081_matrix.txt")
