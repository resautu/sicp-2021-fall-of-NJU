;;; Lab08: Scheme

(define (over-or-under a b)
  (cond
    ((< a b) -1)
    ((= a b) 0)
    ((> a b) 1)
  )
)


(define (make-adder n)
  (
    lambda (x) (+ x n)
  )
)


(define (composed f g)
  (
    lambda (x) (f (g x))
  )
)


(define (remainder a b)
  (- a (* b (quotient a b))))

(define (gcd a b)
  (
    if (= b 0)
      a
      (gcd b (remainder a b))
  )
)


(define lst
  (
    cons 
      (cons 1 nil)
      (cons
        2
        (cons
          (cons 3 (cons 4 nil))
          (cons 5 nil)
        )
      )
  )
)


(define (ordered s)
  (
    cond
    ((= (length s) 0) #t)
    ((= (length s) 1) #t)
    ((<= (car s) (car(cdr s))) (ordered (cdr s)))
    ((> (car s) (car(cdr s))) #f)
  )
)
