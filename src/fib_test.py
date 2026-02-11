import pytest

import fib


@pytest.mark.parametrize(
  ("input", "output"), [(0, 0), (1, 1), (2, 1), (3, 2), (10, 55)]
)
def test_get_nth(input: int, output: int):
  assert fib.get_nth(input) == output
