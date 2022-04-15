;; Student Name: Collin Lowing
;; File Name: part1.lisp
;; Project 4
;;
;; Hard coding given FSA in lisp for testing strings

(defvar filename "theString.txt")

(defun state0(strlist)
  ; end of string, stopping state reached
  (if (= (length strlist) 0)
    (return-from state0 0)) ; not an accept state
  ; Handle transitions
  (let ((sublist strlist) (n 0))
    (dolist (L strlist)
      (cond
        ((STRING-EQUAL L "x") (setf n (+ n 1)))
        ((STRING-EQUAL L "y") (return-from state0 (state1 (subseq sublist (+ n 1) (length sublist))))))))
  (return-from state0 0))

(defun state1(strlist)
  ; end of string, stopping state reached
  (if (= (length strlist) 0)
    (return-from state1 1)) ; accept state
  ; Handle transitions
  (let ((sublist strlist) (n 0))
    (dolist (L strlist)
      (cond
        ((STRING-EQUAL L "x") (return-from state1 (state2 (subseq sublist n (length sublist))))))))
  (return-from state1 0))

(defun state2(strlist)
  ; end of string, stopping state reached
  (if (= (length strlist) 0)
    (return-from state2 0)) ; not an accept state
  ; Handle transitions
  (let ((sublist strlist) (n 0))
    (dolist (L strlist)
      (cond
        ((STRING-EQUAL L "x") (setf n (+ n 1)))
        ((STRING-EQUAL L "y") (return-from state2 (state3 (subseq sublist (+ n 1) (length sublist))))))))
  (return-from state2 0))

(defun state3(strlist)
  ; end of string, stopping state reached
  (if (= (length strlist) 0)
    (return-from state3 1)) ; accept state
  ; Handle transitions
  (let ((sublist strlist) (n 0))
    (dolist (L strlist)career@uwf.edu
      (cond
        ((STRING-EQUAL L "x") (setf n (+ n 1)))
        ((STRING-EQUAL L "z") (return-from state3 (state4 (subseq sublist (+ n 1) (length sublist))))))))
  (return-from state3 0))

(defun state4(strlist)
  ; end of string, stopping state reached
  (if (= (length strlist) 0)
    (return-from state3 0)) ; not an accept state
  ; Handle transitions
  (let ((sublist strlist) (n 0)); Transition Map
    (dolist (L strlist)
      (cond
        ((STRING-EQUAL L "x") (setf n (+ n 1)))
        ((STRING-EQUAL L "a") (return-from state4 (state1 (subseq sublist (+ n 1) (length sublist))))))))
  (return-from state4 0))

; check if string matches alphabet
(defun checkalphabet(str alphabet)
  (dolist (c str)
    (if (find c alphabet)
      (return-from checkalphabet 1)
      (return-from checkalphabet 0))))

(defun demo () "runs the fsa processing"
  (setq file (open filename :direction :input))
  (setq strlist (read file "done"))
  (princ "processing ")
  (terpri)
  (setq current-state 0)
  (setq accept 0)
  (setq alphabet '(x y z a))

  ; variable for determining the string is part of the alphabet
  ; assign from check function 0 or 1 for true or false
  (setq inalphabet (checkalphabet strlist alphabet))


  ; process FSA
  (setq success (state0 strlist))
  ; print out result
  (if (and (= success 1) (= inalphabet 1))
    (write "string is legal") ; success
    (write "string is illegal"))) ; failure
