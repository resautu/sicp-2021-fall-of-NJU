test = {
  'name': 'Problem 6',
  'points': 100,
  'suites': [
    {
      'cases': [
        {
          'answer': 'Another commentary function.',
          'choices': [
            'Another commentary function.',
            'An integer representing the score.',
            'None.'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'What does a commentary function return?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> def echo(s0, s1):
          ...     print(s0, s1)
          ...     return echo
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(3), goal=5, say=echo)
          3 0
          3 3
          7 3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> #
          >>> def count(n):
          ...     def say(s0, s1):
          ...         print(n, s0)
          ...         return count(n + 1)
          ...     return say
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(1), goal=3, say=count(1))
          1 0
          2 0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> #
          >>> def echo(s0, s1):
          ...     print(s0, s1)
          ...     return echo
          >>> strat0 = lambda score, opponent: 1 - opponent // 10
          >>> strat1 = always_roll(3)
          >>> s0, s1 = play(strat0, strat1, dice=make_test_dice(4, 2, 6), goal=15, say=echo)
          5 0
          5 15
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> #
          >>> # Ensure that say is properly updated within the body of play
          >>> def total(s0, s1):
          ...     print(s0 + s1)
          ...     return echo
          >>> def echo(s0, s1):
          ...     print(s0, s1)
          ...     return total
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2, 5), goal=10, say=echo)
          3 0
          8
          5 5
          16
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import play, always_roll
      >>> from dice import make_test_dice
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> def echo_0(s0, s1):
          ...     print('*', s0)
          ...     return echo_0
          >>> def echo_1(s0, s1):
          ...     print('**', s1)
          ...     return echo_1
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2), goal=5, say=both(echo_0, echo_1))
          * 3
          ** 0
          * 3
          ** 3
          * 5
          ** 3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> #
          >>> s0, s1 = play(always_roll(3), always_roll(3), dice=make_test_dice(1, 2, 3, 3), goal=8, say=both(say_scores, announce_lead_changes()))
          Player 0 now has 0 and Player 1 now has 2
          Player 1 takes the lead by 2
          Player 0 now has 0 and Player 1 now has 4
          Player 0 now has 1 and Player 1 now has 4
          Player 0 now has 1 and Player 1 now has 13
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import play, always_roll, both, announce_lead_changes, say_scores
      >>> from dice import make_test_dice
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
