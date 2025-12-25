(defn triangle []
  (setv n 1
        rst 0)
  (while True
    (+= rst n)
    (+= n 1)
    (yield rst)))

(defn pentagonal []
  (setv n 1
        rst 0)
  (while True
    (+= rst n)
    (+= n 3)
    (yield rst)))

(defn hexagonal []
  (setv n 1
        rst 0)
  (while True
    (+= rst n)
    (+= n 4)
    (yield rst)))

(defn sol [n]
  (setv last-pen 0
        last-tri 0
        gen-pen (pentagonal)
        gen-tri (triangle))
  (for [h (hexagonal)]
    (while (< last-pen h)
      (setv last-pen (next gen-pen)))
    (while (< last-tri h)
      (setv last-tri (next gen-tri)))
    (if (= h last-pen last-tri)
        (do (print h)
            (-= n 1)
            (if (= n 0)
                (return h))))))

(sol 3)
