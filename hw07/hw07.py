""" Homework 07: Special Method, Linked List and Tree"""

#####################
# Required Problems #
#####################

class Polynomial:
    """Polynomial.

    >>> a = Polynomial([0, 1, 2, 3, 4, 5, 0])
    >>> a
    Polynomial([0, 1, 2, 3, 4, 5])
    >>> print(a)
    0 + 1*x^1 + 2*x^2 + 3*x^3 + 4*x^4 + 5*x^5
    >>> b = Polynomial([-1, 0, -2, 1, -3])
    >>> print(b)
    -1 + 0*x^1 + -2*x^2 + 1*x^3 + -3*x^4
    >>> print(a + b)
    -1 + 1*x^1 + 0*x^2 + 4*x^3 + 1*x^4 + 5*x^5
    >>> print(a * b)
    0 + -1*x^1 + -2*x^2 + -5*x^3 + -7*x^4 + -12*x^5 + -11*x^6 + -15*x^7 + -7*x^8 + -15*x^9
    >>> print(a)
    0 + 1*x^1 + 2*x^2 + 3*x^3 + 4*x^4 + 5*x^5
    >>> print(b) # a and b should not be changed
    -1 + 0*x^1 + -2*x^2 + 1*x^3 + -3*x^4
    >>> zero = Polynomial([0])
    >>> zero
    Polynomial([0])
    >>> print(zero)
    0
    """
    def __init__(self,st):
      if len(st)==1:
        self.st=st
      else:
        if st[len(st)-1]==0:
          while st[len(st)-1]==0 and len(st)>1:
            st=st[:len(st)-1]
          self.st=st
        else:
          self.st=st
    def __str__(self):
      i=0
      r=''
      for t in self.st:
        if i==0:
          r=str(t)
        else:
          r=r+' + '+str(t)+'*x^'+str(i)
        i+=1
      return r
    def __repr__(self):
      
      return 'Polynomial({0})'.format(self.st)
    def __add__(self,other):
      re=[x+y for x,y in zip(self.st, other.st)]
      if len(self.st)==len(other.st):
        return Polynomial(re)
      elif len(self.st)>len(other.st):
        re+=self.st[len(other.st):]
        return Polynomial(re)
        
      else:
        re+=other.st[len(self.st):]
        return Polynomial(re)
    def __mul__(self,other):
      x1s=list(enumerate(self.st))
      x2s=list(enumerate(other.st))
      i=0
      new_st=[0 for _ in range(len(self.st+other.st)-1)]
      while i<len(self.st+other.st):
        for x1 in x1s:
        
          for x2 in x2s:
            if x1[0]+x2[0]==i:
              new_st[i]+=x1[1]*x2[1]
        i+=1
      return Polynomial(new_st)



def remove_duplicates(lnk):
    """ Remove all duplicates in a sorted linked list.

    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> Link.__init__, hold = lambda *args: print("Do not steal chicken!"), Link.__init__
    >>> try:
    ...     remove_duplicates(lnk)
    ... finally:
    ...     Link.__init__ = hold
    >>> lnk
    Link(1, Link(5))
    """
    if lnk==Link.empty:
      return
    lst=[]
    while True:
      lst+=[lnk.first]
      if lnk.rest==lnk.empty:
        break
      elif lnk.rest.first in lst:
        while lnk.rest!=lnk.empty and lnk.rest.first in lst:
          lnk.rest=lnk.rest.rest
        if lnk.rest==lnk.empty:
          break
      lnk=lnk.rest
        
      



def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> # Disallow the use of making new Links before calling deep_map_mut
    >>> Link.__init__, hold = lambda *args: print("Do not steal chicken!"), Link.__init__
    >>> try:
    ...     deep_map_mut(lambda x: x * x, link1)
    ... finally:
    ...     Link.__init__ = hold
    >>> print(link1)
    <9 <16> 25 36>
    """
    
    while link is not Link.empty:
      if isinstance(link.first, Link) and link.first !=Link.empty:
        deep_map_mut(fn, link.first)
      else:
        link.first = fn(link.first)
      link = link.rest


def reverse(lnk):
    """ Reverse a linked list.

    >>> a = Link(1, Link(2, Link(3)))
    >>> # Disallow the use of making new Links before calling reverse
    >>> Link.__init__, hold = lambda *args: print("Do not steal chicken!"), Link.__init__
    >>> try:
    ...     r = reverse(a)
    ... finally:
    ...     Link.__init__ = hold
    >>> print(r)
    <3 2 1>
    >>> a.first # Make sure you do not change first
    1
    """
    if lnk==Link.empty:
      return lnk
    
    else:
      pre=lnk
      rest=lnk.rest
      pre.rest=Link.empty
      while rest!=Link.empty:
        r=rest.rest
        rest.rest=pre
        pre=rest
        rest=r
      return pre
        
      







class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str

        return print_tree(self).rstrip()
    
    def __eq__(self,other): # Does this line need to be changed?
        """Returns whether two trees are equivalent.

        >>> t1 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)]), Tree(7)])
        >>> t1 == t1
        True
        >>> t2 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)]), Tree(7)])
        >>> t1 == t2
        True
        >>> t3 = Tree(0, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)]), Tree(7)])
        >>> t4 = Tree(1, [Tree(5, [Tree(6)]), Tree(2, [Tree(3), Tree(4)]), Tree(7)])
        >>> t5 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)])])
        >>> t1 == t3 or t1 == t4 or t1 == t5
        False
        """
        if self.label!=other.label:
          return False
        elif self.is_leaf() and other.is_leaf() :
          return self.label == other.label
          
        else:
          i=0
          for x,y in zip(self.branches,other.branches):
            i+=1
            if not Tree.__eq__(x,y):
              return False
          if i<max(len(self.branches),len(other.branches)):
            return False
          return True


def generate_paths(t, value):
    """Yields all possible paths from the root of t to a node with the label value
    as a list.

    >>> t1 = Tree(1, [Tree(2, [Tree(3), Tree(4, [Tree(6)]), Tree(5)]), Tree(5)])
    >>> print(t1)
    1
      2
        3
        4
          6
        5
      5
    >>> next(generate_paths(t1, 6))
    [1, 2, 4, 6]
    >>> path_to_5 = generate_paths(t1, 5)
    >>> sorted(list(path_to_5))
    [[1, 2, 5], [1, 5]]

    >>> t2 = Tree(0, [Tree(2, [t1])])
    >>> print(t2)
    0
      2
        1
          2
            3
            4
              6
            5
          5
    >>> path_to_2 = generate_paths(t2, 2)
    >>> sorted(list(path_to_2))
    [[0, 2], [0, 2, 1, 2]]
    """
    if t.label==value:
      yield [value]
      
      for branch in t.branches:
        for path in generate_paths(branch,value):
          yield [t.label]+path
    else:
      for branch in t.branches:
        for path in generate_paths(branch,value):
          yield [t.label]+path
    


def funcs(link):
    """
    >>> t = Tree(1, [Tree(2,
    ...                   [Tree(5),
    ...                    Tree(6, [Tree(8)])]),
    ...               Tree(3),
    ...               Tree(4, [Tree(7)])])
    >>> print(t)
    1
      2
        5
        6
          8
      3
      4
        7
    >>> func_generator = funcs(Link.empty) # get root label
    >>> f1 = next(func_generator) 
    >>> f1(t)
    1
    >>> func_generator = funcs(Link(2)) # get label of third branch
    >>> f1 = next(func_generator)
    >>> f2 = next(func_generator)
    >>> f2(f1(t))
    4
    >>> # This just puts the 4 values from the iterable into f1, f2, f3, f4
    >>> f1, f2, f3, f4 = funcs(Link(0, Link(1, Link(0))))
    >>> f4(f3(f2(f1(t))))
    8
    >>> f4(f2(f1(t)))
    6
    """
    def index_branch(n):          #make a helper fuction
      def take_branch(t):
        return t.branches[n]
      return take_branch
    if link==Link.empty:
      yield lambda t : t.label
    
    else:
      link_list=[]
      while link!=Link.empty:
        if link.first==Link.empty:
          yield lambda t : t.label
        link_list+=[link.first]
        link=link.rest
      
      
      for inde in link_list:
        yield index_branch(inde)
      yield lambda t : t.label




def count_coins(change, denominations):
    """
    Given a positive integer change, and a list of integers denominations,
    a group of coins makes change for change if the sum of the values of 
    the coins is change and each coin is an element in denominations.
    count_coins returns the number of such groups. 
    """
    if change == 0:
        return 1
    if change < 0:
        return 0
    if len(denominations) == 0:
        return 0
    without_current = count_coins(change, denominations[1:])
    with_current = count_coins(change - denominations[0], denominations)
    return without_current + with_current


def count_coins_tree(change, denominations):
    """
    >>> count_coins_tree(1, []) # Return None since no ways to make change wuth no denominations
    >>> t = count_coins_tree(3, [1, 2]) 
    >>> print(t) # 2 ways to make change for 3 cents
    3, [1, 2]
      2, [1, 2]
        2, [2]
          1
        1, [1, 2]
          1
    >>> # The tree that shows the recursive calls that result
    >>> # in the 6 ways to make change for 15 cents
    >>> t = count_coins_tree(15, [1, 5, 10, 25]) 
    >>> print(t)
    15, [1, 5, 10, 25]
      15, [5, 10, 25]
        10, [5, 10, 25]
          10, [10, 25]
            1
          5, [5, 10, 25]
            1
      14, [1, 5, 10, 25]
        13, [1, 5, 10, 25]
          12, [1, 5, 10, 25]
            11, [1, 5, 10, 25]
              10, [1, 5, 10, 25]
                10, [5, 10, 25]
                  10, [10, 25]
                    1
                  5, [5, 10, 25]
                    1
                9, [1, 5, 10, 25]
                  8, [1, 5, 10, 25]
                    7, [1, 5, 10, 25]
                      6, [1, 5, 10, 25]
                        5, [1, 5, 10, 25]
                          5, [5, 10, 25]
                            1
                          4, [1, 5, 10, 25]
                            3, [1, 5, 10, 25]
                              2, [1, 5, 10, 25]
                                1, [1, 5, 10, 25]
                                  1
    """
    
    a=str(change)+', '+str(denominations)
    if change == 0:
      return Tree(str(1))
    if change < 0:
      return None
    if len(denominations) == 0:
      return None
    b=count_coins_tree(change, denominations[1:])
    c=count_coins_tree(change - denominations[0], denominations)
    if not b and not c:
      t=None
    elif not b:
      t=Tree(a,[c])
    elif not c:
      t=Tree(a,[b])
    
    else:
      t=Tree(a,[b,c])
    return t

def balance_tree(t):
    """Balance a tree.

    >>> t1 = Tree(1, [Tree(2, [Tree(2), Tree(3), Tree(3)]), Tree(2, [Tree(4), Tree(4)])])
    >>> balance_tree(t1)
    >>> t1
    Tree(1, [Tree(2, [Tree(3), Tree(3), Tree(3)]), Tree(3, [Tree(4), Tree(4)])])
    """
    def total_weight(t):
      if t.is_leaf():
        return t.label
      else:
        sum_t=t.label
        for branch in t.branches:
          sum_t+=total_weight(branch)
        return sum_t
    def balance(t):
      if t.is_leaf():
        return  
      max_weight=0
      for branch in t.branches:
        if total_weight(branch)>max_weight:
          
          max_weight=total_weight(branch)
      
      for branch in t.branches:
        
        if total_weight(branch)<max_weight:
          
          branch.label+=max_weight-total_weight(branch)
        
    
    for branch in t.branches:
      
      for branch1 in branch.branches:
        for branch0 in branch1.branches:
          balance(branch0)
        balance(branch1)
      balance(branch) 
    balance(t)
    for branch2 in t.branches:
      balance_tree(branch2)

##########################
# Just for fun Questions #
##########################

def has_cycle(lnk):
    """ Returns whether lnk has cycle.

    >>> lnk = Link(1, Link(2, Link(3)))
    >>> has_cycle(lnk)
    False
    >>> lnk.rest.rest.rest = lnk
    >>> has_cycle(lnk)
    True
    >>> lnk.rest.rest.rest = lnk.rest
    >>> has_cycle(lnk)
    True
    """
    if lnk is Link.empty:
        return False
    
    rest = lnk.rest
    
    while rest != Link.empty:
        if rest == lnk:
            return True
        rest = rest.rest
        

    return False


def install_camera(t):
    """Calculates the minimum number of cameras that need to be installed.

    >>> t = Tree(0, [Tree(0, [Tree(0), Tree(0)])])
    >>> install_camera(t)
    1
    >>> t = Tree(0, [Tree(0, [Tree(0, [Tree(0)])])])
    >>> install_camera(t)
    2
    """
    "*** YOUR CODE HERE ***"


#####################
#        ADT        #
#####################

class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'



