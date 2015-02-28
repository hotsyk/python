from .router import route_from
from nose.tools import eq_


def test_router():
    eq_(route_from(1), {'time': 3, 'checkpoints': [1, 2, 6]})
    eq_(route_from(15), {'time': 12, 'checkpoints': [15, 12, 11, 2, 6]})
    eq_(route_from(17), {'time': 23, 'checkpoints': [17, 16, 13, 11, 2, 6]})
    eq_(route_from(0), {'time': 7, 'checkpoints': [0, 1, 2, 6]})
    eq_(route_from(10), {'time': 20, 'checkpoints': [10, 9, 4, 3, 6]})
    eq_(route_from(7), {'time': 11, 'checkpoints': [7, 12, 11, 2, 6]})
