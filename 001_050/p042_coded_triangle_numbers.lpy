(import [math [sqrt]])

(defn parse [path]
  (with [f (open path "r")]
    (as-> (f.readline) a
        (a.split ",")
        (map (fn [x] (x.strip "\"")) a)
        (list a))))

(defn triangle? [t]
  (setv n (int (sqrt (* 2 t))))
  (= (* 2 t) (* n (+ n 1))))

(defn word-score [word]
  (setv ret (len word))
  (for [c word]
    (+= ret (- (ord c) (ord "A"))))
  ret)

(defn triangle-words [lst]
  (lfor word lst :if (triangle? (word-score word)) word))

(defn sol [path]
  (len (triangle-words (parse path))))

(sol "./p042_words.txt")
