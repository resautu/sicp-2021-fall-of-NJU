def both_odd(a, b):
    """Returns True if both a and b are odd numbers.

    >>> both_odd(-1, 1)
    True
    >>> both_odd(2, 1)
    False
    """
    m=a % 2 ==1 and b % 2 ==1
    return bool(m)


def factorial(n):
    """Return the factorial of a positive integer n.

    >>> factorial(3)
    6
    >>> factorial(5)
    120
    """
    pass  # YOUR CODE HERE
    s=1
    while n>0:
        s=s*n
        n=n-1
    return s


def is_triangle(a, b, c):
    """Given three integers (may be nonpositive), judge whether the three
    integers can form the three sides of a triangle.

    >>> is_triangle(2, 1, 3)
    False
    >>> is_triangle(5, -3, 4)
    False
    >>> is_triangle(2, 2, 2)
    True
    """
    pass  # YOUR CODE HERE
    return a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a and a-b<c and a-c<b and b-c<a and b-a<c and b-c<a and c-a<b


def number_of_six(n):
    """Return the number of 6 in each digit of a positive integer n.

    >>> number_of_six(666)
    3
    >>> number_of_six(123456)
    1
    """
    pass  # YOUR CODE HERE
    y=1
    t=0
    while n>0:
        y=n % 10
        n=n//10
        if y==6:
            t=t+1
    return t
            


def max_digit(x):
    """Return the max digit of x.

    >>> max_digit(10)
    1
    >>> max_digit(4224)
    4
    >>> max_digit(1234567890)
    9
    >>> # make sure that you are using return rather than print
    >>> a = max_digit(123)
    >>> a
    3
    """
    pass  # YOUR CODE HERE
    y=0
    b=0
    while x>0:
        b=x % 10
        x=x//10
        if b>y:
            y=b
    return y

