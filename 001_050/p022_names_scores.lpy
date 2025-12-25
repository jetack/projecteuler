(import [collections [defaultdict]])

(setv path "./p022_names.txt")

(defn parse [path]
  (-> (with [f (open path "r")]
        (f.readline))
      (.split ",")
      (sorted)))

(defn name-sum [s]
  (sum (lfor c s :if (<= (ord "A") (ord c) (ord "Z")) (+ (- (ord c) (ord "A")) 1))))

(defn sol [parsed]
  (sum (lfor (, i s) (enumerate parsed) (* (+ i 1) (name-sum s)))))

(sol (parse path))
