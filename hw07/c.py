if self.st[len(self.st)-1]==0:
        return 'Polynomial({0})'.format(self.st[:len(self.st)-1])


def store_digits(n):
    """Stores the digits of a positive number n in a linked list.
    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    >>> # a check for restricted functions
    >>> import inspect, re
    >>> cleaned = re.sub(r"#.*\\n", '', re.sub(r'"{3}[\s\S]*?"{3}', '', inspect.getsource(store_digits)))
    >>> print("Do not use str or reversed!") if any([r in cleaned for r in ["str", "reversed"]]) else None
    """
    "*** YOUR CODE HERE ***"
    if n<10:
        return Link(n)
    else:
        k = 1
        while(True):
            if 10**k<=n<10**(k+1):
                first,rest = n//10**k, n%10**k
                break
            else:
                k+=1
        return Link(first,store_digits(rest))



def cumulative_mul(t):
    """Mutates t so that each node's label becomes the product of all labels in
    the corresponding subtree rooted at t.
    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_mul(t)
    >>> t
    Tree(105, [Tree(15, [Tree(5)]), Tree(7)])
    """
    "*** YOUR CODE HERE ***"
    if t.is_leaf():
        pass
    else:
        for b in t.branches:
            cumulative_mul(b)
            t.label *= b.label


def has_cycle(link):
    """Return whether link contains a cycle.
    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    "*** YOUR CODE HERE ***"
    if link is Link.empty:
        return False

    rest = link.rest
    while(rest is not Link.empty):
        if rest is link:
            return True
        rest = rest.rest
    return False


if isinstance(lnk.first, Link):
        st=' ' + reverse(lnk.first) +st
        lnk=lnk.rest
        continue

if not t.is_leaf():


 def count_tree(change, denominations, t):
    
        if change == 0:
            return 1
        if change < 0:
            return 0
        if len(denominations) == 0:
            return 0
        without_current = count_tree(change, denominations[1:], t)
        with_current = count_tree(change - denominations[0], denominations, t)
        if without_current==0:
          t.branches=[with_current]
        elif with_current==0:
          t.branches=[without_current]
        else:
          t.branches=[without_current]+[with_current]
        return t
    return count_tree(change, denominations,t)





   if t.is_leaf():
      return  
    max_weight=0
    for branch in t.branches:
      if total_weight(branch)>max_weight:
        
        max_weight=total_weight(branch)
    
    for branch in t.branches:
      
      if total_weight(branch)<max_weight:
        t.label-=max_weight-total_weight(branch)
        branch.label+=max_weight-total_weight(branch)
        
    for branch in t.branches:
      balance_tree(branch)



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
      if not branch.is_leaf():
        for branch1 in branch.branches:
          balance_tree(branch1)
      balance_tree(branch)



def __add__(self,other):
      re=[x+y for x,y in zip(self.st, other.st)]
      if len(self.st)==len(other.st):
        return Polynomial(re)
      elif len(self.st)>len(other.st):
        re.st+=self.st[len(other.st):]
        return Polynomial(re)
        
      else:
        re.st+=other.st[len(self.st):]
        return Polynomial(re)



if link==Link.empty:
      return
    while True:
      
      if isinstance(link.first, Link):
        if link.first!=Link.empty:
          deep_map_mut(fn, link.first)
        if link.rest==link.empty:
          break
        link=link.rest
      
      if link.first!=Link.empty:  
        link.first=fn(link.first)
      if link.rest==link.empty:
        break
      link=link.rest



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
      return '< >'
    elif lnk.rest==lnk.empty:
      return '<' + str(lnk.first) + '>'
    else:
      st='>'
    while lnk.rest!=lnk.empty:
      
      st=' '+str(lnk.first)+st
      lnk=lnk.rest
    st='<'+str(lnk.first)+st
    return st



if lnk==Link.empty:
      return '<()>'
    
    else:
      st='>'
    while lnk.rest!=Link.empty:
      
      st=' '+str(lnk.first)+st
      lnk=lnk.rest
    st='<'+str(lnk.first)+st
    return st



pre=lnk
      
      lnk=lnk.rest



 if lnk==Link.empty or lnk.rest==Link.empty:
      return 
    
    else:
      pre=lnk
      
      
      while lnk!=Link.empty:
        rest=lnk.rest
        lnk.rest=pre
        pre=lnk
        lnk=rest
      lnk=pre


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
    def index_branch(n):
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
      
      link_list.reverse()
      for inde in link_list:
        yield index_branch(inde)
      yield lambda t : t.label


if link==Link.empty:
      yield lambda t : t.label
    else:
      while link!=Link.empty:
        yield lambda t : t.branches[link.first]
        link=link.rest
      yield lambda t : t.label 