;;; hy==1.0a4


(import time [time])

;;; integer functions
(defn gcd [x y]
  (setv [x y] [(min x y) (max x y)])
  (while (> x 0)
    (setv [x y] [(% y x) x]))
  y)

(defn lcm [x y]
  (* x (// y (gcd x y))))

;;; rational numbers functions
(defn frac-reduce [x]
  (setv [xn xd] x
        [xn xd] (if (< xd 0) [(- xn) (- xd)] [xn xd])
        div (gcd (abs xn) xd))
  [(// xn div) (// xd div)])

(defn frac-add [x y]
  (setv [xn xd] x
        [yn yd] y
        denom (lcm xd yd)
        numer (+ (* xn (// denom xd))
                 (* yn (// denom yd))))
  (frac-reduce [numer denom]))

(defn frac-mul [x y]
  (setv [xn xd] x
        [yn yd] y
        denom (* xd yd)
        numer (* xn yn))
  (frac-reduce [numer denom]))

(defn frac-neg [x]
  (setv [xn xd] x)
  [(- xn) xd])

(defn reciprocal [x]
  (setv [xn xd] x)
  [xd xn])

(defn digit-sum [x]
  (setv rst 0)
  (while x
    (+= rst (% x 10))
    (//= x 10))
  rst)

(defn solution [[n 33]]
  (setv seq [2]
        rst [1 1])
  (for [i (range 1 (+ n 1))]
    (seq.append 1)
    (seq.append (* 2 i))
    (seq.append 1))
  (seq.pop)
  (while seq
    (setv rst (frac-add [(seq.pop) 1] (reciprocal rst))))
  (digit-sum (get rst 0)))

(defn main []
  (setv start (time))
  (print (solution))
  (print "elapsed:" (- (time) start)))

(main)
