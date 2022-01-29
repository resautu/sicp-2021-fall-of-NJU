test = {
  'name': 'Problem 10',
  'points': 100,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> picky_piggy_strategy(0, 6, cutoff=9, num_rolls=5)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> picky_piggy_strategy(9, 0, cutoff=6, num_rolls=5)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> picky_piggy_strategy(50, 3, cutoff=8, num_rolls=5)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> picky_piggy_strategy(32, 0, cutoff=8, num_rolls=4)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> picky_piggy_strategy(20, 0, cutoff=1, num_rolls=4)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> from tests.check_strategy import check_strategy
          >>> check_strategy(picky_piggy_strategy)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
