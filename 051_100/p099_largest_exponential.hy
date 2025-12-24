;;; hy==1.0a4
(import hyrule *)
(require hyrule *)

(import math [log])

(defn parse [path]
  (with [f (open path "r")]
    (lfor line (f.readlines) (as-> line x
                                   (x.strip)
                                   (x.split ",")
                                   (map int x)
                                   (list x)))))

(defn project [base exponent]
  (+ (log exponent) (log (log base))))

(defn sol [parsed]
  (max (range (len parsed)) :key (fn [i] (setv x (get parsed i)) (project #* x))))

(print (+ 1 (sol (parse "./p099_base_exp.txt"))))
