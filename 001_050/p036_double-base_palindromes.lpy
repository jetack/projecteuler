(defn 10-palindrome? [n]
  (setv lst [])
  (while n
    (lst.append (% n 10))
    (//= n 10))
  (lst-palindrome? lst))

(defn lst-palindrome? [lst]
  (setv n (len lst))
  (for [i (range (// n 2))]
    (if (!= (get lst i) (get lst (- n 1 i)))
        (return False)))
  True)

(defn sol [limit]
  (setv ret []
        l-max (- (len (bin limit)) 2))
  (defn recur [b [ret ret] [l-max l-max]]
    (setv num (if b (int b 2) 0))
    (if (>= num limit)
        ret
        (do
          (when (and num (10-palindrome? num))
            (ret.append num))
          (for [i (range (// (- l-max 1) 2))]
            (recur (+ "1" (* "0" i) b (* "0" i) "1") ret)))))
  (recur "")
  (recur "1")
  (recur "0")
  ret)

(sum (sol (** 10 6)))

