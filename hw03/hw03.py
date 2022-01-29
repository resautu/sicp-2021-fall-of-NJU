""" Homework 3: Recursion and Tree Recursion"""

HW_SOURCE_FILE = 'hw03.py'

#####################
# Required Problems #
#####################

def number_of_six(n):
    """Return the number of 6 in each digit of a positive integer n.

    >>> number_of_six(666)
    3
    >>> number_of_six(123456)
    1
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'number_of_six',
    ...       ['Assign', 'AugAssign'])
    True
    """
    def lls1(n):
        if n//10==0 and n%6!=0:
            return 0
        elif n//10==0 and n%6==0:
            return 1
        elif n//10!=0 and n%10==6:
            return 1+lls1(n//10)
        else:
            return lls1(n//10)
    return lls1(n)
            


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    5
    >>> pingpong(8)
    4
    >>> pingpong(15)
    3
    >>> pingpong(21)
    5
    >>> pingpong(22)
    6
    >>> pingpong(30)
    10
    >>> pingpong(68)
    0
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    -1
    >>> pingpong(72)
    -2
    >>> pingpong(100)
    6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    def change(ls):
        return -ls
    def lls2(n,ls):
        if n==1:
            return 1
        elif n%6==0 or number_of_six(n)>0:
            return lls2(n-1,change(ls))-ls
        else:
            return lls2(n-1,ls)+ls
    def cs1(n):
        if n==0:
            return 0
        elif number_of_six(n)>0:
            return cs1(n-1)+1
        elif number_of_six(n)==0 and n%6==0:
            return cs1(n-1)+1
        else:
            return cs1(n-1)
    if cs1(n)%2==0:
        return lls2(n,1)
    else:
        return lls2(n,-1)


def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    if n//10==0:
        return 0
    elif n%10==n//10%10+1:
        return missing_digits(n//10)
    elif n%10!=n//10%10+1 and n%10!=n//10%10:
        if n%10==n//10%10+2:
            return missing_digits(n//10)+1
        elif n%10==n//10%10+3:
            return missing_digits(n//10)+2
        elif n%10==n//10%10+4:
            return missing_digits(n//10)+3
        elif n%10==n//10%10+5:
            return missing_digits(n//10)+4
        elif n%10==n//10%10+6:
            return missing_digits(n//10)+5
        elif n%10==n//10%10+7:
            return missing_digits(n//10)+6
    else:
        return missing_digits(n//10)


def count_change(total, next_money):
    """Return the number of ways to make change for total,
    under the currency system described by next_money.

    >>> def chinese_yuan(money):
    ...     if money == 1:
    ...         return 5
    ...     if money == 5:
    ...         return 10
    ...     if money == 10:
    ...         return 20
    ...     if money == 20:
    ...         return 50
    ...     if money == 50:
    ...         return 100
    >>> def us_cent(money):
    ...     if money == 1:
    ...         return 5
    ...     elif money == 5:
    ...         return 10
    ...     elif money == 10:
    ...         return 25
    >>> count_change(15, chinese_yuan)
    6
    >>> count_change(49, chinese_yuan)
    44
    >>> count_change(49, us_cent)
    39
    >>> count_change(49, lambda x: x * 2)
    692
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_change', ['While', 'For'])
    True
    """
    def lls4(x,y):
        if x==0:
            return 1
        elif x<0:
            return 0
        elif y==None:
            return 0
        elif y>x:
            return 0
        
        
        else:
            zj=lls4(x-y,y)
            pj=lls4(x,next_money(y))
            return zj+pj
    money=1
    return lls4(total,money)


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)


def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    lst=[1,2,3]
    lst.remove(start)
    lst.remove(end)
    mid=lst[0]
    def hnt(n,start,mid,end):
        if n==1:
            print_move(start,end)
        else:
            hnt(n-1,start,end,mid)
            print_move(start,end)
            hnt(n-1,mid,start,end)
    return hnt(n,start,mid,end)


def multiadder(n,x=0):
    """Return a function that takes N arguments, one at a time, and adds them.
    >>> f = multiadder(3)
    >>> f(5)(6)(7) # 5 + 6 + 7
    18
    >>> multiadder(1)(5)
    5
    >>> multiadder(2)(5)(6) # 5 + 6
    11
    >>> multiadder(4)(5)(6)(7)(8) # 5 + 6 + 7 + 8
    26
    >>> from construct_check import check
    >>> # Make sure multiadder is a pure function.
    >>> check(HW_SOURCE_FILE, 'multiadder',
    ...       ['Nonlocal', 'Global'])
    True
    """
    
    
    def lls6(m):
        
        return multiadder(n-1,x+m)

    
    if n>0:   
        return lls6
    else:
        return x


##########################
# Just for fun Questions #
##########################


from operator import sub, mul


def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    
    return lambda x ,i : x*i for i in range (x) 


Y = lambda f: (lambda x: x(x))(lambda x: f(lambda z: x(x)(z)))
fib_maker = lambda f: lambda r: 'YOUR_EXPRESSION_HERE'
number_of_six_maker = lambda f: lambda r: 'YOUR_EXPRESSION_HERE'

my_fib = Y(fib_maker)
my_number_of_six = Y(number_of_six_maker)

# This code sets up doctests for my_fib and my_number_of_six.

my_fib.__name__ = 'my_fib'
my_fib.__doc__="""Given n, returns the nth Fibonacci nuimber.

>>> my_fib(0)
0
>>> my_fib(1)
1
>>> my_fib(2)
1
>>> my_fib(3)
2
>>> my_fib(4)
3
>>> my_fib(5)
5
"""

my_number_of_six.__name__ = 'my_number_of_six'
my_number_of_six.__doc__="""Return the number of 6 in each digit of a positive integer n.

>>> my_number_of_six(666)
3
>>> my_number_of_six(123456)
1
"""
