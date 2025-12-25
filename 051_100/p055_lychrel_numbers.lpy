(defmacro do-sth [#* body]
  (setv [condition body] [(get body -1) (get body (slice None -2))])
  `(do
     ~@body
     (while ~condition
       ~@body)))

(defn palindrome? [n]
  (= (str n) (get (str n) (slice None None -1))))

(defn lychrel? [n]
  (setv limit 50)
  (do-sth
    (setv n (+ n (int (get (str n) (slice None None -1)))))
    (-= limit 1)
    :while (and limit (not (palindrome? n))))
  (= limit 0))

(defn sol [n]
  (len (list (filter lychrel? (range 10000)))))

(sol 10000)
