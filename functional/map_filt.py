# naive python implementation of higher order functions: map, filter, polynomial evaluate
import operator
import math

# map
# apply unary function to each element in seqence, return new sequence
def m_map(f,seq):
    result = []
    for elt in seq:
        result.append(f(elt))
    return result

# filter
# test each element of sequence with unary predicate, return new list of elements that satisfy predicate
def m_filter(f,seq):
    result = []
    for elt in seq:
        if f(elt):
            result.append(elt)
    return result


# Suppose we have a polynomial represented as a list of coefficients, a[0], a[1], ..., a[n-1], where a[i] is the coefficient of xi.
def poly_evaluate(a, x):
    xi = map(lambda i: x**i, range(0, len(a))) # [x^0, x^1, x^2, ..., x^(n-1)]
    axi = map(operator.mul, a, xi)             # [a[0]*x^0, a[1]*x^1, ..., a[n-1]*x^(n-1)]
    return reduce(operator.add, axi, 0)        # sum of axi