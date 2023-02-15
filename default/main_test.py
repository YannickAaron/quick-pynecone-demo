"""
proof that main works
"""

from lib import calculator


def test_add() -> None:
    """
    Test add function
    """
    assert calculator.add(1, 2) == 3
