import pytest

import fib


@pytest.mark.parametrize(
  ("n", "expected"), [(0, 0), (1, 1), (2, 1), (3, 2), (10, 55)]
)
def test_get_nth(n: int, expected: int):
  assert fib.get_nth(n) == expected
