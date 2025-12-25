(require [hy.contrib.loop [loop]])

(defn digit-sum [n]
  (loop [[n n] [ret 0]]
        (if n
            (recur (// n 10) (+ ret (% n 10)))
            ret)))

(digit-sum (<< 1 1000))
