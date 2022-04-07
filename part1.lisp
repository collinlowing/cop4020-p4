;; Student Name: Collin Lowing
;; File Name: part1.lisp
;; Project 4
;;
;; Hard coding given FSA in lisp for testing strings

(defvar filename "theString.txt")

(defun demo () "runs the fsa processing"
  (write filename)
  (terpri)
  (setq file (open filename :direction :input))
  (setq strlist (read file "done"))
  (princ "processing ")
  (terpri)
  (princ strlist)
  (terpri)
  (setq current-state 0)
  (setq accept 0)
  (setq alphabet '(x y z a))
  (princ alphabet)
  (terpri)

  (dolist (c strlist)
     (write c)
    (terpri)
    (if (find c alphabet)
      (princ "character is in alphabet")
      (princ "character is not in alphabet"))
    (terpri))

  (if (= accept 1)
    (write "string is legal")
    (write "string is illegal")))
