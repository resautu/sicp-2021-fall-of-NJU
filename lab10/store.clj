(define (filter-stream f s)
  (if (null? s) nil
      (let ((rest (filter-stream f (cdr-stream s))))
        (if (f (car s))
            (cons-stream (car s) rest)
            rest))))


((and (null? (cdr-stream s)) (> (length ist) 1)) nil)



(define (nondecrease s)
  (define (helper s ist)
    (
      cond
        
        ((null? s) (cons-stream nil nil))
        
        
        ((null? (cdr-stream s)) (cons-stream (append ist (list (car s))) nil))
        ((> (car s) (car (cdr-stream s))) (cons-stream (append ist (list (car s))) (helper (cdr-stream s) nil)))
        (else (helper (cdr-stream s) (append ist (list (car s)))))
    )
  )
  (helper s nil)
)

(define (nondecrease s)
  (define (helper s ist p)
    (
      cond
        
        ((null? s) (cons-stream nil nil))
        ((= p 888) (cons-stream ist nil))
        
        ((null? (cdr-stream s)) (cons-stream (append ist (list (car s))) nil))
        ((> (car s) (car (cdr-stream s))) (cons-stream (append ist (list (car s))) (helper (cdr-stream s) nil (+ p 1))))
        (else (helper (cdr-stream s) (append ist (list (car s))) (+ p 1)))
    )
  )
  (helper s nil 0)
)


(define (nondecrease s)
  (
    cond
      ((null? (cdr-stream s)) (cons-stream (list (car s)) nil))
      ((> (car s) (car (cdr-stream s))) (cons-stream (cons (car s) nil) (nondecrease (cdr-stream s))))
      (else (cons-stream (cons (car s) (car (nondecrease (cdr-stream s)))) (cdr-stream (nondecrease (cdr-stream s)))))
  )
)

(define (nondecrease s)
  
  (
    cond
      
      ((null? (cdr-stream s)) (cons-stream (list (car s)) nil))
      
      ((> (car s) (car (cdr-stream s))) (cons-stream (cons (car s) nil) (nondecrease (cdr-stream s))))
      (else (cons-stream (cons (car s) (car (nondecrease (cdr-stream s)))) (cdr-stream (nondecrease (cdr-stream s)))))
  )
  
)


(define fibs
  (cons-stream 0 (cons-stream 1 (combine-with - fibs (cdr-stream fibs))))
)

(cons-stream 1 (combine-with * factorials (naturals 1)))
(cons-stream 0 (cons-stream 1 (combine-with + fibs (cdr-stream fibs))))