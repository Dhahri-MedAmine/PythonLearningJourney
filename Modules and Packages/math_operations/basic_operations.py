"""
Basic Mathmatical Operations
"""

from numbers import Number


def add(a: Number, b: Number) -> Number:
    """Return the sum of 'a' and 'b'

    Args:
        a (Number): 1st number
        b (Number): 2nd number

    Returns:
        Number: sum of 'a' and 'b'
    """
    return a + b  # type: ignore
