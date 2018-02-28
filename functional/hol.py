# high order functions
import operator
import math

# flatten nested sublists into one list
def flatten(list):
    return reduce(operator.concat, list, [])

def compose(f, g):
    """Requires that f and g are functions, f:A->B and g:B->C.
    Returns a function A->C by composing f with g.""" 
    return lambda x: g(f(x))

def chain(funcs):
    """Requires funcs is a list of functions [A->B, B->C, ..., Y->Z]. 
    Returns a fn A->Z that is the left-to-right composition of funcs."""
    return reduce(compose, funcs)

# returns functions that are useful as filters, it takes a filename suffix and dynamically generates a function to use with filter to test for that suffix
def fileEndsWith(suffix):
    return lambda file: file.getName().endsWith(suffix)

