""" Homework 4: Data Abstraction and Trees"""

from ADT import make_city, get_name, get_lat, get_lon, tree, label, branches, is_leaf, print_tree

#####################
# Required Problems #
#####################

def couple(lst1, lst2):
    """Return a list that contains lists with i-th elements of two sequences
    coupled together.
    >>> lst1 = [1, 2, 3]
    >>> lst2 = [4, 5, 6]
    >>> couple(lst1, lst2)
    [[1, 4], [2, 5], [3, 6]]
    >>> lst3 = ['c', 6]
    >>> lst4 = ['s', '1']
    >>> couple(lst3, lst4)
    [['c', 's'], [6, '1']]
    """
    assert len(lst1) == len(lst2)
    
    di=[]
    i=0
    while i<len(lst1):
      di=di+[[lst1[i],lst2[i]]]
      i+=1
    return di

from math import sqrt
def distance(city1, city2):
    """
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    >>> city3 = make_city('city3', 6.5, 12)
    >>> city4 = make_city('city4', 2.5, 15)
    >>> distance(city3, city4)
    5.0
    """
    return sqrt(((get_lat(city1)-get_lat(city2))**2)+((get_lon(city1)-get_lon(city2))**2))

def closer_city(lat, lon, city1, city2):
    """
    Returns the name of either city1 or city2, whichever is closest to
    coordinate (lat, lon).

    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    """
    lls=make_city('lls',lat,lon)
    if distance(city1,lls)<distance(city2,lls):
      return get_name(city1)
    else:
      return get_name(city2)

def nut_finder(t):
    """Returns True if t contains a node with the value 'nut' and
    False otherwise.

    >>> scrat = tree('nut')
    >>> nut_finder(scrat)
    True
    >>> sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('nut')]), tree('branch2')])
    >>> nut_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> nut_finder(numbers)
    False
    >>> t = tree(1, [tree('nut',[tree('not nut')])])
    >>> nut_finder(t)
    True
    """
    if is_leaf(t):
      if label(t)=='nut':
        return True
      else:
        return False
    elif label(t)=='nut':
      return True
    else:
      digit=[nut_finder(branch) for branch in branches(t)]
      return any(digit)

def sprout_leaves(t, values):
    """Sprout new leaves containing the data in values at each leaf in
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    if is_leaf(t):
      return tree(label(t),[tree(value) for value in values])
    else:
      return tree(label(t),[sprout_leaves(branch,values) for branch in branches(t)])

def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    if is_leaf(t1) and is_leaf(t2):
      return tree(label(t1)+label(t2))
    elif len(branches(t1))==len(branches(t2)):
      label1=label(t1)+label(t2)
      digit=[]
      for branch1,branch2 in zip(branches(t1),branches(t2)):
        digit+=[add_trees(branch1,branch2)]
      return tree(label1,digit)
    elif len(branches(t1))>len(branches(t2)):
      label1=label(t1)+label(t2)
      digit=[]
      for branch1,branch2 in zip(branches(t1),branches(t2)):
        digit+=[add_trees(branch1,branch2)]
      digit1=branches(t2)+branches(t1)
      digit+=digit1[2*len(branches(t2)):]
      
        
      return tree(label1,digit)
    else:
      label1=label(t1)+label(t2)
      digit=[]
      for branch1,branch2 in zip(branches(t1),branches(t2)):
        digit+=[add_trees(branch1,branch2)]
      digit1=branches(t1)+branches(t2)
      digit+=digit1[2*len(branches(t1)):]
        
      return tree(label1,digit)


        


def bigpath(t, n):
    """Return the number of paths in t that have a sum larger or equal to n.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> bigpath(t, 3)
    4
    >>> bigpath(t, 6)
    2
    >>> bigpath(t, 9)
    1
    """
    def lls(t,m=0):
      if is_leaf(t):
        m=m+label(t)
        nonlocal n
        if m>=n:
          return 1
        else:
          return 0
      else:
        i=0
        if m+label(t)>=n:
          su=1
        else:
          su=0
        
        while i<len(branches(t)):
          su+=lls(branches(t)[i],m+label(t))
          i+=1
        return su
    return lls(t)


def bigger_path(t, n):
    """Return the number of paths in t that have a sum larger or equal to n.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> bigger_path(t, 3)
    9
    >>> bigger_path(t, 6)
    4
    >>> bigger_path(t, 9)
    1
    """
    def lls_bigger(t,n):
      

      def lls(t,m=0):
        if is_leaf(t):
          m=m+label(t)
          nonlocal n
          if m>=n:
            return 1
          else:
            return 0
        else:
          i=0
          if m+label(t)>=n:
            su=1
          else:
            su=0
        
          while i<len(branches(t)):
            su+=lls(branches(t)[i],m+label(t))
            i+=1
          return su
      
      if is_leaf(t):
        
        if label(t)>=n:
          return 1
        else:
          return 0
      else:
        
        i=0
        s=0
        while i<len(branches(t)):
          s=s+lls_bigger(branches(t)[i],n)
          i+=1
        s+=lls(t,m=0)
        return s
    return lls_bigger(t,n)

  
      
      



##########################
# Just for fun Questions #
##########################

def fold_tree(t, base_func, merge_func):
    """Fold tree into a value according to base_func and merge_func"""
    "*** YOUR CODE HERE ***"

def count_leaves(t):
    """Count the leaves of a tree.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> count_leaves(t)
    3
    """
    return fold_tree(t, 'YOUR EXPRESSION HERE', 'YOUR EXPRESSION HERE')

def label_sum(t):
    """Sum up the labels of all nodes in a tree.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> label_sum(t)
    15
    """
    return fold_tree(t, 'YOUR EXPRESSION HERE', 'YOUR EXPRESSION HERE')

def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> preorder(t)
    [1, 2, 3, 4, 5]
    """
    return fold_tree(t, 'YOUR EXPRESSION HERE', 'YOUR EXPRESSION HERE')
