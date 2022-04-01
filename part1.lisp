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
  (setq list (read file "done"))
  (princ "processing ")
  (terpri)
  (princ list)
  (terpri)
  (setq current-state 0)
  (setq accept 0)
  (loop for c in list
    do (princ c)
      (terpri)
      (cond ((and (= current-state 0)
                (STRING-EQUAL c "x")
                (progn
                 (setq current-state 0)
                 (setq accept 0))))
           (and (= current-state 0
                 (STRING-EQUAL c "y")
                 (progn
                  (setq current-state 1)
                  (setq accept 1)))

              (and (= current-state 1
                    (STRING-EQUAL c "x")
                    (progn
                     (setq current-state 2)
                     (setq accept 0))))

              (and (= current-state 2
                    (STRING-EQUAL c "x")
                    (progn
                     (setq current-state 2)
                     (setq accept 0))))

              (and (= current-state 2
                    (STRING-EQUAL c "y")
                    (progn
                     (setq current-state 3)
                     (setq accept 1))))
              (and (= current-state 3
                    (STRING-EQUAL c "x")
                    (progn
                     (setq current-state 3)
                     (setq accept 1))))

              (and (= current-state 3
                    (STRING-EQUAL c "z")
                    (progn
                     (setq current-state 4)
                     (setq accept 0))))

              (and (= current-state 4
                    (STRING-EQUAL c "x")
                    (progn
                     (setq current-state 4)
                     (setq accept 0))))

              (and (= current-state 4
                    (STRING-EQUAL c "a")
                    (progn
                     (setq current-state 1)
                     (setq accept 1))))
              (t (error "illegal char in string")))))

  (if (= accept 1)
    (write "string is legal")
    (write "string is illegal")))
