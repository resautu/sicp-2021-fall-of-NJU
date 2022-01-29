(define (find-nest n sym)          ;I have used frame of cs61a!!!
  (define (search-n s exp)
  (
    cond
      ((number? s) (if (= s n) '(car) nil))
      ((null? s) nil)
      (else (search-list s exp))
  
  )
  )
  (define (search-list s exp)
    (
      let
        (
          (first (search-n (car s) exp))
          (rest (list (search-n (cdr s) exp) '(cdr)))
        )
        (if (null? first) rest first)
    )
  )
  (search-n (eval sym) sym)
)



(define-macro (let* bindings expr)
  (
    let
    (
      (y 2)
    )
    y
  )
)

(define-macro (let* bindings expr)
  (list
    'cond
    (list (list 'null? bindings) expr)
    (list 'else (list 'let (list (list (list 'car (list 'car bindings)) (list 'car bindings)) (list 'let* (list 'cdr bindings) expr))))
  )
)


(list 'define (cons func args) body)
let
    (
      (rest (except args indices 0))
      (sub (make args vals indices 0))
    )
    (list 'lambda rest (cons fn sub))