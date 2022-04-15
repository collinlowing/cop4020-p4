;; Student Name: Collin Lowing
;; File Name: part1.lisp
;; Project 4
;;
;; Hard coding given FSA in lisp for testing strings

(defvar filename "theString.txt")

(defun state0(stringlist)
  ; end of string, stopping state reached
  (if (= (length stringlist) 0)
    (return-from state0 0)) ; not an accept state
  ; Handle transitions
  (let ((sublist stringlist) (n 0))
    (dolist (char stringlist)
      (cond
        ((STRING-EQUAL char "x") (setf n (+ n 1)))
        ((STRING-EQUAL char "y") (return-from state0 (state1 (subseq sublist (+ n 1) (length sublist))))))))
  (return-from state0 0))

(defun state1(stringlist)
  ; end of string, stopping state reached
  (if (= (length stringlist) 0)
    (return-from state1 1)) ; accept state
  ; Handle transitions
  (let ((sublist stringlist) (n 0))
    (dolist (char stringlist)
      (cond
        ((STRING-EQUAL char "x") (return-from state1 (state2 (subseq sublist n (length sublist))))))))
  (return-from state1 0))

(defun state2(stringlist)
  ; end of string, stopping state reached
  (if (= (length stringlist) 0)
    (return-from state2 0)) ; not an accept state
  ; Handle transitions
  (let ((sublist stringlist) (n 0))
    (dolist (char stringlist)
      (cond
        ((STRING-EQUAL char "x") (setf n (+ n 1)))
        ((STRING-EQUAL char "y") (return-from state2 (state3 (subseq sublist (+ n 1) (length sublist))))))))
  (return-from state2 0))

(defun state3(stringlist)
  ; end of string, stopping state reached
  (if (= (length stringlist) 0)
    (return-from state3 1)) ; accept state
  ; Handle transitions
  (let ((sublist stringlist) (n 0))
    (dolist (char stringlist)career@uwf.edu
      (cond
        ((STRING-EQUAL char "x") (setf n (+ n 1)))
        ((STRING-EQUAL char "z") (return-from state3 (state4 (subseq sublist (+ n 1) (length sublist))))))))
  (return-from state3 0))

(defun state4(stringlist)
  ; end of string, stopping state reached
  (if (= (length stringlist) 0)
    (return-from state3 0)) ; not an accept state
  ; Handle transitions
  (let ((sublist stringlist) (n 0)); Transition Map
    (dolist (char stringlist)
      (cond
        ((STRING-EQUAL char "x") (setf n (+ n 1)))
        ((STRING-EQUAL char "a") (return-from state4 (state1 (subseq sublist (+ n 1) (length sublist))))))))
  (return-from state4 0))

; check if string matches alphabet
(defun checkalphabet(str alphabet)
  (dolist (c str)
    (if (find c alphabet)
      (return-from checkalphabet 1)
      (return-from checkalphabet 0))))

(defun demo () "runs the fsa processing"
  (setq file (open filename :direction :input))
  (setq stringlist (read file "done"))
  (princ "processing ")
  (terpri)
  (setq current-state 0)
  (setq accept 0)
  (setq alphabet '(x y z a))

  ; variable for determining the string is part of the alphabet
  ; assign from check function 0 or 1 for true or false
  (setq inalphabet (checkalphabet stringlist alphabet))


  ; process FSA
  (setq success (state0 stringlist))
  ; print out result
  (if (and (= success 1) (= inalphabet 1))
    (princ "string is legal") ; success
    (princ "string is illegal"))) ; failure
