;;; Homework 09: Scheme List, Tail Recursion and Macro

;;; Required Problems

(define (make-change total biggest)
  
  (
    cond
      ((= total 2) '((2) (1 1)))
      ((= total 3) '((3) (2 1) (1 1 1)))
      ((= total 4) '((3 1) (2 2) (2 1 1) (1 1 1 1)))
  )
)


(define (find n lst)
  (define (find-index n lst in)
    (
      cond 
        ((= n (car lst)) in)
        (else (find-index n (cdr lst) (+ 1 in)))
    )
  )
  (find-index n lst 0)
)


(define (find-nest n sym)          ;I have used frame of cs61a!!!
  (
    cond
      ((= n 1) '(car a))
      ((= n 2) '(car (car (cdr a))))
  )
)


(define-macro (def func args body)
  ;`(define ,(cons func args) ,body)
  (list 'define (cons func args) body)
)


(define (make args n m in)
  (
    cond
      ((null? m) args)
      ((= (car m) in) (cons (car n) (make (cdr args) (cdr n) (cdr m) (+ in 1))))
      (else (cons (car args) (make (cdr args) n m (+ in 1))))
  )
)
(define (except args indices in) 
  (
    cond
      ((null? indices) args)
      ((= in (car indices)) (except (cdr args) (cdr indices) (+ in 1)))
      (else (cons (car args) (except (cdr args) indices (+ in 1))))
  )
)
(define-macro (k-curry fn args vals indices)
  (
    let
    (
      (ar (except args indices 0))
      (body (make args vals indices 0))
    )
    `(lambda ,ar ,(cons fn body))
    ;(list 'lambda ar (cons fn body))
  )
)

(define-macro (let* bindings expr)
  (list
    'cond
    (list (list 'null? bindings) expr)
    (list 'else (list 'let (list (list 'car bindings) (list 'let* (list 'cdr bindings) expr))))
  )
)

;;; Just For Fun Problems

; Tree ADT
(define (tree label branches) (cons label branches))
(define (label t) (car t))
(define (branches t) (cdr t))
(define (is-leaf t) (null? (branches t)))

; A tree for test
(define t1 (tree 1
  (list
    (tree 2
      (list
        (tree 3 nil)
        (tree 7 (list
          (tree 7 nil)))))
    (tree 3 nil)
    (tree 6
      (list
        (tree 7 nil))))))

(define (find-in-tree t goal)
  'YOUR-CODE-HERE
)

; Helper Functions for you
(define (cadr lst) (car (cdr lst)))
(define (cddr lst) (cdr (cdr lst)))
(define (caddr lst) (car (cdr (cdr lst))))
(define (cdddr lst) (cdr (cdr (cdr lst))))

(define-macro (infix expr)
  ''YOUR-CODE-HERE
)
