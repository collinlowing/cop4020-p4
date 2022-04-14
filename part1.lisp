;; Student Name: Collin Lowing
;; File Name: part1.lisp
;; Project 4
;;
;; Hard coding given FSA in lisp for testing strings

(defvar filename "theString.txt")

(defun Node0(ls)
  ; end of string, stopping state reached
  (if (= (length ls) 0)
    (return-from Node0 0)) ; not an accept state
  ; Handle transitions
  (let ((lss ls) (n 0))
    (dolist (L ls)
      (cond
        ((STRING-EQUAL L "x") (setf n (+ n 1)))
        ((STRING-EQUAL L "y") (return-from Node0 (Node1 (subseq lss (+ n 1) (length lss))))))
      (if (> n 0) (write "n > 0"))))
  (return-from Node0 0))

(defun Node1(ls)
  ; end of string, stopping state reached
  (if (= (length ls) 0)
    (return-from Node1 1)) ; accept state
  ; Handle transitions
  (let ((lss ls) (n 0))
    (dolist (L ls)
      (cond
        ((STRING-EQUAL L "x") (return-from Node1 (Node2 (subseq lss n (length lss))))))))
  (return-from Node1 0))

(defun Node2(ls)
  ; end of string, stopping state reached
  (if (= (length ls) 0)
    (return-from Node2 0)) ; not an accept state
  ; Handle transitions
  (let ((lss ls) (n 0))
    (dolist (L ls)
      (cond
        ((STRING-EQUAL L "x") (setf n (+ n 1)))
        ((STRING-EQUAL L "y") (return-from Node2 (Node3 (subseq lss (+ n 1) (length lss))))))))
  (return-from Node2 0))

(defun Node3(ls)
  ; end of string, stopping state reached
  (if (= (length ls) 0)
    (return-from Node3 1)) ; accept state
  ; Handle transitions
  (let ((lss ls) (n 0))
    (dolist (L ls)
      (cond
        ((STRING-EQUAL L "x") (setf n (+ n 1)))
        ((STRING-EQUAL L "z") (return-from Node3 (Node4 (subseq lss (+ n 1) (length lss))))))))
  (return-from Node3 0))

(defun Node4(ls)
  ; end of string, stopping state reached
  (if (= (length ls) 0)
    (return-from Node3 0)) ; not an accept state
  ; Handle transitions
  (let ((lss ls) (n 0)); Transition Map
    (dolist (L ls)
      (cond
        ((STRING-EQUAL L "x") (setf n (+ n 1)))
        ((STRING-EQUAL L "a") (return-from Node4 (Node1 (subseq lss (+ n 1) (length lss))))))))
  (return-from Node4 0))

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

  ; check if string matches alphabet
  (dolist (c strlist)
     (write c)
    (terpri)
    (if (find c alphabet)
      (princ "character is in alphabet")
      (princ "character is not in alphabet"))
    (terpri))

  ; process transitions
  (princ (Node0 strlist))
  (terpri)
  (if (= (Node0 strlist) 1)
    (write "string is legal") ; success
    (write "string is illegal"))) ; failure
