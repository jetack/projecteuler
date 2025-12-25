(defn non-zero-digits [n]
  (setv ret [])
  (while n
    (setv r (% n 10))
    (if r (ret.append (% n 10))) 
    (//= n 10))
  ret)

(defn limit [n]
  (setv 9-to-n (** 9 n)
        i 1)
  (while (< (** 10 i) (* i 9-to-n))
    (+= i 1))
  i)

(defn nth-sum [digits n]
  (sum (lfor d digits (** d n))))

(defn sol [n]
  (setv ret [])
  (for [i (range (** 10 (limit n)))]
    (setv nz-digits (non-zero-digits i))
    (if (and (> (len nz-digits) 1)
             (= i (nth-sum nz-digits n)))
        (ret.append i)))
  (sum ret))

(sol 5)
