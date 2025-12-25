(import [hy.contrib.loop [__trampoline__]])

(with-decorator __trampoline__
  (defn fact [n [ret 1]]
    (if (< n 2) ret
        (fact (- n 1) (* ret n)))))

(defn digit-sum [n]
  (setv ret 0)
  (while n
    (+= ret (% n 10))
    (//= n 10))
  ret)

(digit-sum (fact 100))
