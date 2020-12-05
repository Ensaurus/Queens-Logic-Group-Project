from functools import total_ordering
from os import umask
from nnf import Var
from lib204 import Encoding

from nnf import true

import varSetup
from display import display_solution

#For using iff(F1,F2), >> for implication and ~ for negation.
from nnf import NNF
from nnf.operators import iff

def implication(l, r):
    return l.negate() | r

def neg(f):
    return f.negate()

NNF.__rshift__ = implication
NNF.__invert__ = neg

A = Var("A")
B = Var("B")

def test_theory():
    E = Encoding()
    E.add_constraint(A | B)

    return E

def add_A(T):
    T.add_constraint(A)
    T.add_constraint(B)
    return T

def remove_A(T):
    T.remove_constraint(A)
    return T
def remove_B(T):
    T.remove_constraint(B)
    return T

if __name__ == "__main__":
    T = test_theory()
    print("\nSatisfiable: %s" % T.is_satisfiable())
    print("# Solutions: %d" % T.count_solutions())

    T = add_A(T)
    print("\nSatisfiable: %s" % T.is_satisfiable())
    print("# Solutions: %d" % T.count_solutions())

    T = remove_A(T)
    print("\nSatisfiable: %s" % T.is_satisfiable())
    print("# Solutions: %d" % T.count_solutions())

    T = remove_B(T)
    print("\nSatisfiable: %s" % T.is_satisfiable())
    print("# Solutions: %d" % T.count_solutions())