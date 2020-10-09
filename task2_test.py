#!python3

import assignment

def test1():
    assert list(assignment.factorPair(24,12)) == [2,12]
    assert list(assignment.factorPair(40,1)) == [1,40]