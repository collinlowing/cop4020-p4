(defvar filename "theString.txt")


(defun demo () "runs the fsa processing"
  (write filename)
  (terpri)
  (setq file (open filename :direction :input))
  (setq list (read file "done"))
  (princ "processing ")
  (terpri)
  (princ list))
