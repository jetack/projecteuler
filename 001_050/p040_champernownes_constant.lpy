(defn sol [lst]
  (setv d-num 1
        l 10
        cur 1
        ret [])
  (for [i lst]
    (while (< (* d-num (- l (// l 10))) (- i cur))
      (+= cur (* d-num (- l (// l 10))))
      (+= d-num 1)
      (*= l 10))
    (ret.append (int (get (str (+ (// l 10)
                                  (// (- i cur) d-num)))
                          (% (- i cur) d-num)))))
  (reduce * ret))

(sol (lfor i (range 7) (** 10 i)))
