(import [collections [defaultdict]]
        [pprint [pprint]])

(defn parse [path]
  (setv prevs (defaultdict set)
        afters (defaultdict set)
        occurs (set))
  (with [f (open path "r")]
    (for [line f]
      (setv line (list (map int (list (line.strip)))))
      (for [v line]
        (occurs.add v))
      (for [i (range 2)]
        (for [j (range (+ i 1) 3)]
          (.add (get afters (get line i)) (get line j))
          (.add (get prevs (get line j)) (get line i))))))
  [prevs afters occurs])

(defn check-multiple-presents [prevs afters occurs]
  (for [i occurs]
    (if (len (.intersection (get prevs i) (get afters i)))
        (raise ValueError))))

(defn pick-and-update [prevs occurs]
  (for [i occurs]
    (if (= 0 (len (get prevs i)))
        (do (occurs.remove i)
            (for [j occurs]
              (.remove (get prevs j) i))
            (return [prevs occurs i])))))

(defn sol [path]
  (setv [prevs afters occurs] (parse path)
        rst 0)
  (check-multiple-presents prevs afters occurs)
  (while occurs
    (setv [prevs occurs next-value] (pick-and-update prevs occurs))
    (*= rst 10)
    (+= rst next-value))
  rst)

(sol "./p079_keylog.txt")
