;;; Lab 10: Stream

;;; Required Problems

;(define (filter-stream f s)
;  (if (null? s) nil
;      (let ((rest (filter-stream f (cdr s))))
;        (if (f (car s))
;            (cons-stream (car s) rest)
;            rest))))
(define (filter-stream f s)
  (
    cond 
      ((null? s) nil)
      ((f (car s)) (cons-stream (car s) (filter-stream f (cdr-stream s))))
      (else (filter-stream f (cdr-stream s)))
  )
)

(define (slice s start end)
  (define (helper s start end index)
    (
      cond
        ((> start end) nil)
        ((null? s) nil)
        ((< index start) (helper (cdr-stream s) start end (+ index 1)))
        ((= index end) nil)
        (else (cons (car s) (helper (cdr-stream s) start end (+ index 1))))
    )
  )
  (helper s start end 0)
)


(define (naturals n)
  (cons-stream n (naturals (+ n 1))))


(define (combine-with f xs ys)
  (if (or (null? xs) (null? ys))
      nil
      (cons-stream
        (f (car xs) (car ys))
        (combine-with f (cdr-stream xs) (cdr-stream ys)))))


(define factorials
  (cons-stream 1 (combine-with * (naturals 1) factorials))
)


(define fibs
  (cons-stream 0 (cons-stream 1 (combine-with + fibs (cdr-stream fibs))))
)


(define (exp x)
  (cons-stream 1 (combine-with + (combine-with / (combine-with (lambda (x1 x2) (expt x x1)) (naturals 1) (naturals 1)) (cdr-stream factorials)) (exp x)))
)

(define (list-to-stream lst)
  (if (null? lst) nil
      (cons-stream (car lst) (list-to-stream (cdr lst)))))


(define (nondecrease s)
  (define (helper s ist)
    (
      cond
        
        ((null? s) nil)
        
        
        ((null? (cdr-stream s)) (cons-stream (append ist (list (car s))) nil))
        ((> (car s) (car (cdr-stream s))) (cons-stream (append ist (list (car s))) (helper (cdr-stream s) nil)))
        (else (helper (cdr-stream s) (append ist (list (car s)))))
    )
  )
  (helper s nil)
)

;;; Just For Fun Problems

(define-macro (my-cons-stream first second) ; Does this line need to be changed?
  `(cons-stream ,first ,second)
)

(define (my-car stream)
  (eval (car stream))
)

(define (my-cdr-stream stream)
  (eval (car (cdr-stream stream)))
)


(define (sieve s)
  'YOUR-CODE-HERE
)

(define primes (sieve (naturals 2)))
