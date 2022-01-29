test = {
  'name': 'Problem 1',
  'points': 300,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> roll_dice(1, 2, make_test_dice(4, 6, 1))
          10
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> roll_dice(1, 3, make_test_dice(4, 6, 1))
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> roll_dice(0, 4, make_test_dice(2, 2, 3))
          12
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> a = roll_dice(0, 4, make_test_dice(1, 2, 3))
          >>> a # check that the value is being returned, not printed
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> counted_dice = make_test_dice(4, 1, 2, 6)
          >>> roll_dice(0, 3, counted_dice)
          3
          >>> # Make sure you call dice exactly num_rolls times!
          >>> # If you call it fewer or more than that, it won't be at the right spot in the cycle for the next roll
          >>> # Note that a return statement within a loop ends the loop
          >>> roll_dice(0, 1, counted_dice)
          7
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> roll_dice(1, 9, make_test_dice(6))
          54
          >>> roll_dice(0, 7, make_test_dice(2, 2, 2, 2, 2, 2, 1))
          7
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
