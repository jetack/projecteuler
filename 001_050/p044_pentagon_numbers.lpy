(import [time [time]])

(defmacro do-sth [#* body]
  (setv [condition body] [(get body -1) (get body (slice None -2))])
  `(do
     ~@body
     (while ~condition
       ~@body)))

(defn pentagon-gen []
  (setv n 0
        x -2)
  (while True
    (+= x 3)
    (+= n x)
    (yield n)))

(defn update [lst hsh n]
  (lst.append n)
  (hsh.add n))

(defn sol []
  (setv list-mem []
        hash-mem (set)
        pen-gen (pentagon-gen)
        rst -1)
  (for [_ (range 4)]
    (update list-mem hash-mem (next pen-gen)))
  (setv i 1)
  (do-sth
    (setv iv (get list-mem i))
    (setv j (- i 1))
    (setv jv (get list-mem j))
    (while (< (get list-mem -1) (+ jv iv))
      (update list-mem hash-mem (next pen-gen)))
    (do-sth
      (if (and (in (- iv jv) hash-mem)
               (in (+ iv jv) hash-mem))
          (setv rst (if (< rst 0)
                        (- iv jv)
                        (min rst (- iv jv)))))
      (-= j 1)
      (setv jv (get list-mem j))
      :while (and (> j 0) (or (< rst 0) (< (- iv jv) rst))))
    (+= i 1)
    :while (or (< rst 0) (> rst (+ (* 3 i) 1))))
  rst)

(do
  (setv t (time))
  (print (sol))
  (print (- (time) t)))
