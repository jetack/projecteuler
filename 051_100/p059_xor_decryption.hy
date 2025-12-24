;;; hy==1.0a4

(defn parse [path]
  (with [f (open path "r")]
    (as-> (f.readline) x
          (x.strip)
          (x.split ",")
          (map int x)
          (list x))))

(defn decrypt [encrypted key]
  (setv l (len key))
  (lfor [i c] (enumerate encrypted) (^ c (get key (% i l)))))

(defn seq-to-str [seq]
  (.join "" (lfor c seq (chr c))))

(defn decrypted? [decrypted-str]
  ;; started with ["the" "and"], when I added space after these words, only one decryption satisfies this condition
  (setv common-words ["the " "and "])
  (and #* (lfor w common-words (in w decrypted-str))))

(defn sol [encrypted]
  (setv lower-cases (range (ord "a") (+ (ord "z") 1)))
  (for [i lower-cases]
    (for [j lower-cases]
      (for [k lower-cases]
        (setv decrypted (decrypt encrypted [i j k]))
        (when (decrypted? (seq-to-str decrypted))
          (print (seq-to-str decrypted))
          (return (sum decrypted)))))))

(print (sol (parse "./p059_cipher.txt")))
