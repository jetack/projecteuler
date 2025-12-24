;;; hy==1.0a4

(import time [time]
        collections [Counter defaultdict])

(defn char-to-num [c]
  (setv d {"T" 10 "J" 11 "Q" 12 "K" 13 "A" 14})
  (if (in c d)
      (get d c)
      (int c)))

(defn parse-hand [hand]
  (setv suits (set)
        nums [])
  (for [card hand]
    (suits.add (get card 1))
    (nums.append (char-to-num (get card 0))))
  (setv c2num (defaultdict list))
  (for [[n c] (.items (Counter nums))]
    (.append (get c2num c) n))
  (for [v (c2num.values)]
    (v.sort))
  [(= 1 (len suits)) (sorted nums :reverse True) c2num])

(defn straight? [nums]
  (for [i (range 4)]
    (if (!= (get nums i) (+ (get nums (+ i 1)) 1))
        (return False)))
  True)

(defn four-card? [cnt]
  (if (in 4 cnt)
      [True (get cnt 4)]
      [False None]))

(defn house? [cnt]
  (if (and (in 3 cnt) (in 2 cnt))
      [True [(get cnt 3) (get cnt 2)]]
      [False None]))

(defn three-card? [cnt]
  (if (in 3 cnt)
      [True (get cnt 3)]
      [False None]))

(defn calc-hand [hand]
  (setv [f? nums cnt] (parse-hand hand)
        s? (straight? nums))
  (if (and s? f?)
      (return [8 nums]))
  (setv [made? rep] (four-card? cnt))
  (if made?
      (return [7 nums]))
  (setv [made? rep] (house? cnt))
  (if made?
      (return [6 rep nums]))
  (if f?
      (return [5 nums]))
  (if s?
      (return [4 nums]))
  (setv [made? rep] (three-card? cnt))
  (if made?
      (return [3 rep nums]))
  (setv pairs (get cnt 2))
  [(len pairs) pairs nums])

(defn leftwin? [cards]
  (setv left-hand (cut cards None 5)
        right-hand (cut cards 5 None)
        left-stat (calc-hand left-hand)
        right-stat (calc-hand right-hand))
  (> left-stat right-stat))

(defn solution []
  (with [f (open "./p054_poker.txt")]
    (setv lines (f.readlines)))
  ;; (setv lines ["5H 5C 6S 7S KD 2C 3S 8S 8D TD"
  ;;              "5D 8C 9S JS AC 2C 5C 7D 8S QH"
  ;;              "2D 9C AS AH AC 3D 6D 7D TD QD"
  ;;              "4D 6S 9H QH QC 3D 6D 7H QD QS"
  ;;              "2H 2D 4C 4D 4S 3C 3D 3S 9S 9D"])
  (sum (lfor line lines (leftwin? (.split (.strip line) " ")))))

(defn main []
  (setv start (time))
  (print (solution))
  (print "elapsed:" (- (time) start)))

(main)
